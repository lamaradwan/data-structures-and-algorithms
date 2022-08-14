from trees.trees import Node, BinaryTree
from hashtable.hashtable import HashTable


def tree_intersection(t1, t2):
    ht = HashTable()
    for i in range(len(t1)):
        if t1[i] == t2[i]:
            ht.set(str(t1[i]), 1)
    return ht.key()


if __name__ == '__main__':
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

    # print(tree.pre_order())
    # print(tree2.pre_order())
    print(tree_intersection(tree.pre_order(), tree2.pre_order()))
