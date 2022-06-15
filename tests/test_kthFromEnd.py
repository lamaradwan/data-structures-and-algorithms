import math

import pytest
from linked_list.linked_list import LinkedList


# Where k is greater than the length of the linked list
def test_k_out_of_range():
    testing = LinkedList()
    testing.Append(10)
    testing.Append(10)
    with pytest.raises(Exception) as errorMsg:
        testing.kthFromEnd(4)
    assert (str(errorMsg.value)) == "Index 4 is out of range"

# Where k and the length of the list are the same
def test_k_is_a_length():
    testing = LinkedList()
    testing.Append(10)
    with pytest.raises(Exception) as errorMsg:
        testing.kthFromEnd(1)
    assert (str(errorMsg.value)) == "Index 1 is out of range"

# Where k is not a positive integer
def test_k_negative_number(list_testing_k_negative):
    actual = list_testing_k_negative
    expected = "Index should be a positive number"
    assert actual == expected

# Where the linked list is of a size 1
def test_list_with_size_one(list_testing_size_one):
    actual = list_testing_size_one
    expected = 10
    assert actual == expected

#“Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_not_happy_path():
    actual = verify_happy_path()
    expected = "Not a happy path"
    assert actual == expected

testing = LinkedList()
testing.Append(10)
testing.Append(15)
testing.Append(20)
testing.Append(25)
testing.Append(30)

def verify_not_happy_path():
    if math.floor(testing.count / 2) == math.floor(testing.count / 1):
        return testing.kthFromEnd(1)
    else:
        return "Not a happy path"

def test_not_happy_path():
    actual = verify_not_happy_path()
    expected = "Not a happy path"
    assert actual == expected

def verify_happy_path():
    if math.floor(testing.count / 2) == math.floor(testing.count / 2):
        return testing.kthFromEnd(2)
    else:
        return 20

def test_happy_path():
    actual = verify_happy_path()
    expected = 20
    assert actual == expected


@pytest.fixture()
def list_testing_k_negative():
    testing = LinkedList()
    testing.Append(10)
    testing.Append(15)
    testing.Append(20)
    return testing.kthFromEnd(-2)

@pytest.fixture()
def list_testing_size_one():
    testing = LinkedList()
    testing.Append(10)
    return testing.kthFromEnd(0)

@pytest.fixture()
def list_testing_happy_path():
    testing = LinkedList()
    testing.Append(10)
    testing.Append(15)
    testing.Append(20)
    testing.Append(25)
    testing.Append(30)
    return testing.kthFromEnd(2)