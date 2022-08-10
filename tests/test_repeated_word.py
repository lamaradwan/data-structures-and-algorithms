from hashmap_repeated_word.hashmap_repeated_word import repeated_word


def test_capital_words():
    actual = repeated_word('Lama Hiring, she is hiRING for a QA Engineer')
    expected = 'hiring'
    assert actual == expected


def test_small_text():
    actual = repeated_word('once upon a time, there was a brave princess')
    expected = 'a'
    assert actual == expected


def test_not_repeated():
    actual = repeated_word('Hello, are you okay?')
    expected = None
    assert actual == expected
