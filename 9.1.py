def popular_words(text: str, words: list[str]) -> dict[str, int]:
    """
    Counts how many times each target word appears in the given text, case-insensitively.

    :param text: A string containing the source text.
    :param words: A list of lowercase words to search for.
    :return: A dictionary where keys are the target words and values are their counts in the text.
    """
    text_words = text.lower().split()
    return {word: text_words.count(word) for word in words}

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
