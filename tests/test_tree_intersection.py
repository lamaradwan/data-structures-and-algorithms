from tree_intersection.tree_intersection import tree_intersection
from trees.trees import BinaryTree, Node

import pytest

def test_common_values():
    tree = BinaryTree()
    tree.root = Node(20)
    tree.root.left = Node(23)
    tree.root.right = Node(10)
    tree.root.left.left = Node(24)
    tree.root.left.right = Node(18)
    tree.root.right.left = Node(100)
    tree.root.right.right = Node(12)

    tree2 = BinaryTree()
    tree2.root = Node(20)
    tree2.root.left = Node(3)
    tree2.root.right = Node(5)
    tree2.root.left.left = Node(24)
    tree2.root.left.right = Node(6)
    tree2.root.right.left = Node(100)
    tree2.root.right.right = Node(12)

    actual = tree_intersection(tree.in_order(), tree2.in_order())
    expected = ['24', '20', '100', '12']
    assert actual == expected

def test_uncommon_values():
    tree = BinaryTree()
    tree.root = Node(0)
    tree.root.left = Node(3)
    tree.root.right = Node(0)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(8)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(2)

    tree2 = BinaryTree()
    tree2.root = Node(20)
    tree2.root.left = Node(37)
    tree2.root.right = Node(5)
    tree2.root.left.left = Node(24)
    tree2.root.left.right = Node(6)
    tree2.root.right.left = Node(100)
    tree2.root.right.right = Node(12)

    actual = tree_intersection(tree.in_order(), tree2.in_order())
    expected = []
    assert actual == expected

def test_negative_values():
    tree = BinaryTree()
    tree.root = Node(-20)
    tree.root.left = Node(3)
    tree.root.right = Node(0)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(8)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(2)

    tree2 = BinaryTree()
    tree2.root = Node(-20)
    tree2.root.left = Node(63)
    tree2.root.right = Node(5)
    tree2.root.left.left = Node(24)
    tree2.root.left.right = Node(6)
    tree2.root.right.left = Node(100)
    tree2.root.right.right = Node(12)

    actual = tree_intersection(tree.in_order(), tree2.in_order())
    expected = ['-20']
    assert actual == expected
