import pytest
from insertion_sort.insertion_sort import insertion_sort

def test_sortion():
    actual = insertion_sort([8,3,2,4])
    expected = [2,3,4,8]
    assert actual == expected


def test_sorted_list():
    actual = insertion_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

def test_duplicated_values_list():
    actual = insertion_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_negative_values_list():
    actual = insertion_sort([20, -18, 12, 8, 5, -2])
    expected = [-18, -2, 5, 8, 12, 20]
    assert actual == expected

def test_one_index():
    actual = insertion_sort([1])
    expected = [1]
    assert actual == expected

def test_empty_list():
    actual = insertion_sort([])
    expected = 'Empty List'
    assert actual == expected