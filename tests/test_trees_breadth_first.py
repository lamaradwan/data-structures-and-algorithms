import pytest
from trees_breadth_first.trees_breadth_first import breadth_first
from trees.trees import Node,BinaryTree

def test_order_letters(letters_tree):
    actual = letters_tree
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    assert actual == expected

@pytest.fixture()
def letters_tree():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    return tree.breadth_first()

def test_empty_tree():
    tree = BinaryTree()
    actual = tree.breadth_first()
    expected = None
    assert actual == expected