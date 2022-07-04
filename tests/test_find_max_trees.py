import pytest
from trees.trees import BinaryTree, Node

# return root when the maximum value is the root
def test_maximum_root(maximum_root):
    actual = maximum_root
    expected = 200
    assert actual == expected

@pytest.fixture()
def maximum_root():
    tree = BinaryTree()
    tree.root = Node(200)
    tree.root.left = Node(23)
    tree.root.right = Node(10)
    tree.root.left.left = Node(24)
    tree.root.left.right = Node(18)
    tree.root.right.left = Node(100)
    tree.root.right.right = Node(12)
    return tree.find_maximum()

# return the maximum value on the left
def test_maximum_left(maximum_left):
    actual = maximum_left
    expected = 100
    assert actual == expected

@pytest.fixture()
def maximum_left():
    tree = BinaryTree()
    tree.root = Node(20)
    tree.root.left = Node(23)
    tree.root.right = Node(10)
    tree.root.left.left = Node(24)
    tree.root.left.right = Node(18)
    tree.root.right.left = Node(100)
    tree.root.right.right = Node(12)
    return tree.find_maximum()

# return the maximum value on the right
def test_maximum_right(maximum_right):
    actual = maximum_right
    expected = 160
    assert actual == expected


@pytest.fixture()
def maximum_right():
    tree = BinaryTree()
    tree.root = Node(20)
    tree.root.left = Node(23)
    tree.root.right = Node(160)
    tree.root.left.left = Node(24)
    tree.root.left.right = Node(180)
    tree.root.right.left = Node(100)
    tree.root.right.right = Node(12)
    return tree.find_maximum()


# return None if the tree is empty
def test_empty_tree():
    tree = BinaryTree()
    actual = tree.find_maximum()
    expected = None
    assert actual == expected