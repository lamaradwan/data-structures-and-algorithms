import pytest
from trees.trees import Node, BinaryTree, BinarySearchTree


# Can successfully instantiate an empty tree
def test_instantiate_empty_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


# Can successfully instantiate a tree with a single root node
def test_instantiate_tree_with_single_root():
    tree = BinaryTree()
    tree.root = Node(4)
    actual = tree.root.value
    expected = 4
    assert actual == expected


# For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_binary_search_add(binary_search_tree):
    actual = binary_search_tree
    expected = 8
    assert actual == expected


@pytest.fixture()
def binary_search_tree():
    bTree = BinarySearchTree()
    bTree.add(23)
    bTree.add(8)
    bTree.add(42)
    return bTree.root.left.value


# Can successfully return a collection from a preorder traversal
def test_pre_order(pre_order_tree):
    actual = pre_order_tree
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual == expected

@pytest.fixture()
def pre_order_tree():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    return tree.pre_order()


# Can successfully return a collection from an inorder traversal
def test_in_order(in_order_tree):
    actual = in_order_tree
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    assert actual == expected

@pytest.fixture()
def in_order_tree():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    return tree.in_order()

# Can successfully return a collection from a postorder traversal
def test_post_order(post_order_tree):
    actual = post_order_tree
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual == expected

@pytest.fixture()
def post_order_tree():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    return tree.post_order()

# Returns true or false for the contains method, given an existing or non-existing node value
def test_contains_true(contains_tree):
    actual = contains_tree
    expected = True
    assert actual == expected

@pytest.fixture()
def contains_tree():
    bTree = BinarySearchTree()
    bTree.add(23)
    bTree.add(8)
    bTree.add(42)
    bTree.add(4)
    return bTree.contains(4)

def test_contains_false(contains_tree_false):
    actual = contains_tree_false
    expected = False
    assert actual == expected

@pytest.fixture()
def contains_tree_false():
    bTree = BinarySearchTree()
    bTree.add(23)
    bTree.add(8)
    bTree.add(42)
    bTree.add(6)
    return bTree.contains(4)
