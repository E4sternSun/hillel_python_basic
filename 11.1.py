# Образність і контекст — це ключ до розуміння.
# Навчання програмуванню з 0, на мою думку, має
# будуватися на прикладах, які викликають інтерес,
# а не на нескінченних числах заради чисел.
# ось як роблю дз і не тільки цю, спочатку привожу
# до розуміння, а потім вже роблю саме завдання...
#
# def car_generator(max_cylinders: int):
#     """
#     Генерує автомобілі з парною кількістю циліндрів, не більше заданого ліміту.
#
#     :param max_cylinders: Максимально допустима кількість циліндрів.
#     :return: Генератор, що повертає назви автомобілів з парною кількістю циліндрів.
#     """
#     cars = {
#         'Toyota Corolla': 4,
#         'Ford Mustang': 8,
#         'Honda Civic': 4,
#         'Chevrolet Camaro': 6,
#         'Volkswagen Beetle': 5,
#         'BMW M3': 6,
#         'Mazda RX-8': 2,
#         'Lada Niva': 4
#     }
#
#     for name, cylinders in cars.items():
#         if cylinders % 2 == 0 and cylinders <= max_cylinders:
#             yield name
def prime_generator(end: int):
    """
    Генерує прості числа від 2 до заданого значення включно.

    :param end: Ціле число, що визначає верхню межу діапазону.
    :return: Генератор, який повертає прості числа менші або рівні end.
    """
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
