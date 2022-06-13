#####
#This File contains a unit tests for Append, InsertBefore, and InsertAfter methods
#####

import pytest
from linked_list.linked_list import LinkedList

# Can successfully add a node to the end of the linked list
def test_Append(data_for_append):
    actual = data_for_append
    expected = [20, 15, 10, 25]
    assert actual == expected

# Can successfully add multiple nodes to the end of a linked list
def test_multiple_append(data_for_multiple_append):
    actual = data_for_multiple_append
    expected = [25, 30, 35, 40]
    assert actual == expected

# Can successfully insert a node before a node located in the middle of a linked list
def test_insert_before_middle_node(data_for_insert_before_middle):
    actual = data_for_insert_before_middle
    expected = [10, 20, 25, 30, 40]
    assert actual == expected

# Can successfully insert a node before the first node of a linked list
def test_insert_before_first_node(data_for_insert_before_first):
    actual = data_for_insert_before_first
    expected = [5, 10]
    assert actual == expected

# Can successfully insert after a node in the middle of the linked list
def test_insert_after_middle_node(data_for_insert_after_middle):
    actual = data_for_insert_after_middle
    expected = [10, 20, 25, 30, 40]
    assert actual == expected

# Can successfully insert a node after the last node of the linked list
def test_insert_after_last_node(data_for_insert_after_last):
    actual = data_for_insert_after_last
    expected = [10, 20, 30, 40, 50]
    assert actual == expected

@pytest.fixture()
def data_for_append():
    testing = LinkedList()
    testing.Insert(10)
    testing.Insert(15)
    testing.Insert(20)
    testing.Append(25)
    return testing.ToString()

@pytest.fixture()
def data_for_multiple_append():
    testing = LinkedList()
    testing.Append(25)
    testing.Append(30)
    testing.Append(35)
    testing.Append(40)
    return testing.ToString()

@pytest.fixture()
def data_for_insert_before_middle():
    testing = LinkedList()
    testing.Append(10)
    testing.Append(20)
    testing.Append(30)
    testing.Append(40)
    testing.InsertBefore(30,25)
    return testing.ToString()


@pytest.fixture()
def data_for_insert_before_first():
    testing = LinkedList()
    testing.Insert(10)
    testing.InsertBefore(10,5)
    return testing.ToString()

@pytest.fixture()
def data_for_insert_after_middle():
    testing = LinkedList()
    testing.Append(10)
    testing.Append(20)
    testing.Append(30)
    testing.Append(40)
    testing.InsertAfter(20,25)
    return testing.ToString()

@pytest.fixture()
def data_for_insert_after_last():
    testing = LinkedList()
    testing.Append(10)
    testing.Append(20)
    testing.Append(30)
    testing.Append(40)
    testing.InsertAfter(40,50)
    return testing.ToString()
