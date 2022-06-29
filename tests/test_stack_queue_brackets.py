import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_string1():
    actual = validate_brackets("{}")
    expected = True
    assert actual == expected


def test_string2():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected


def test_string3():
    actual = validate_brackets("(){}[[]]")
    expected = True
    assert actual == expected


def test_string4():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected


def test_string5():
    actual = validate_brackets("{}(){}")
    expected = True
    assert actual == expected


def test_string6():
    actual = validate_brackets("[({}]")
    expected = False
    assert actual == expected


def test_string7():
    actual = validate_brackets("(](")
    expected = False
    assert actual == expected


def test_string8():
    actual = validate_brackets("{(})")
    expected = False
    assert actual == expected


def test_string9():
    actual = validate_brackets("l{ama{student})}")
    expected = False
    assert actual == expected


def test_string10():
    actual = validate_brackets("{")
    expected = False
    assert actual == expected


def test_string11():
    actual = validate_brackets("{)")
    expected = False
    assert actual == expected
