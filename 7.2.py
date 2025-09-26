def correct_sentence(text: str) -> str:
    """
    Corrects a sentence so that it starts with a capital letter and ends with a period.

    :param text: The input sentence.
    :type text: str
    :return: The corrected sentence with a capitalized first letter and a period at the end.
    """
    text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('OK')
