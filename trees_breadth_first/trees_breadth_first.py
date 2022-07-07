from trees.trees import Node, BinaryTree, Queue


def breadth_first(self):
    if not self.root:
        return self.root
    output = []
    queue = Queue()
    queue.enqueue(self.root)
    while not queue.isEmpty():
        front = queue.dequeue()
        output.append(front.value)
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)
    return output


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")


    print("++++++++ breadth first +++++++++")
    print(tree.breadth_first())