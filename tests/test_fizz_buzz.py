from tree_fizz_buzz.tree_fizz_buzz import Node, KAry
import pytest

def test_empty_kary_tree(empty_kary_tree):
    actual = empty_kary_tree
    expected = None
    assert actual == expected

@pytest.fixture()
def empty_kary_tree():
    kary = KAry()
    return kary.fizz_buzz_tree()


def test_fizz_buzz_tree(kary_tree):
    actual = kary_tree
    expected = ['Fizz', 2, 4, 'Buzz', 4, 1, 7, 'FizzBuzz']
    assert actual == expected


@pytest.fixture()
def kary_tree():
    kary = KAry()
    kary.root = Node(3)
    kary.root.children.append(Node(2))
    kary.root.children.append(Node(1))
    kary.root.children.append(Node(7))
    kary.root.children[0].children.append(Node(4))
    kary.root.children[0].children.append(Node(5))
    kary.root.children[0].children.append(Node(4))
    kary.root.children[2].children.append(Node(15))
    return kary.fizz_buzz_tree().pre_order()