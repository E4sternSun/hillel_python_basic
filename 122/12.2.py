class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.name}, price: {self.price}'

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'dimensions': self.dimensions
        }

    @staticmethod
    def from_dict(data):
        return Item(
            data['name'],
            data['price'],
            data['description'],
            data['dimensions']
        )
class User:
    def __init__(self, name, surname, number_phone):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone

    def __str__(self):
        return f'{self.name} {self.surname}'

    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'number_phone': self.number_phone
        }

    @staticmethod
    def from_dict(data):
        return User(
            data['name'],
            data['surname'],
            data['number_phone']
        )
class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        return sum(item.price * qty for item, qty in self.products.items())

    def __str__(self):
        lines = [f'User: {self.user}']
        lines.append('Items:')
        for item, qty in self.products.items():
            lines.append(f'{item.name}: {qty} pcs.')
        return '\n'.join(lines)

    def to_dict(self):
        return {
            'user': self.user.to_dict(),
            'products': [
                {'item': item.to_dict(), 'quantity': qty}
                for item, qty in self.products.items()
            ],
            'total': self.get_total()
        }

    @staticmethod
    def from_dict(data):
        user = User.from_dict(data['user'])
        purchase = Purchase(user)
        for entry in data['products']:
            item = Item.from_dict(entry['item'])
            qty = entry['quantity']
            purchase.add_item(item, qty)
        return purchase
