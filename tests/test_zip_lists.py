#####
#This File contains a unit tests for zip lists method
#####

import pytest
from linked_list.linked_list import LinkedList
from zip_lists.zip_lists import zipLists

list1 = LinkedList()
list1.Append(1)
list1.Append(3)
list1.Append(2)

list2 = LinkedList()
list2.Append(5)
list2.Append(9)
list2.Append(4)

def test_list1_equal_to_list2():
    actual = zipLists(list1,list2)
    expected = [1, 5, 3, 9, 2, 4]
    assert actual == expected

list3 = LinkedList()
list3.Append(1)
list3.Append(3)

list4 = LinkedList()
list4.Append(5)
list4.Append(9)
list4.Append(4)

def test_list1_smaller_than_list2():
    actual = zipLists(list3,list4)
    expected = [1, 5, 3, 9, 4]
    assert actual == expected


list5 = LinkedList()
list5.Append(1)
list5.Append(3)
list5.Append(2)

list6 = LinkedList()
list6.Append(5)
list6.Append(9)

def test_list1_larger_than_list2():
    actual = zipLists(list5,list6)
    expected = [1, 5, 3, 9, 2]
    assert actual == expected









