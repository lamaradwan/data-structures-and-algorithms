from stack_and_queue.stack_and_queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):
            result.append(root.value)

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return result

    def in_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):

            if root.left:
                _walk(root.left)

            result.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return result

    def post_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            result.append(root.value)

        _walk(self.root)
        return result


class BinarySearchTree(BinaryTree):

    def add(self, added):
        if not self.root:
            self.root = Node(added)

        def _walk(root):
            if added < root.value:
                if root.left:
                    _walk(root.left)
                else:
                    root.left = Node(added)
            elif added > root.value:
                if root.right:
                    _walk(root.right)
                else:
                    root.right = Node(added)

        _walk(self.root)

    def contains(self, search_for):
        if not self.root:
            return False

        def _walk(root):
            if search_for == root.value:
                # print("true")
                return True

            else:
                try:
                    if search_for < root.value:
                        # print("left")
                        return _walk(root.left)

                    elif search_for > root.value:
                        # print("right")
                        return _walk(root.right)
                except:
                    return False

        if _walk(self.root) == None:
            return False
        else:
            return _walk(self.root)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    print("++++++++ pre order +++++++++")
    print(tree.pre_order())
    print("++++++++ in order +++++++++")
    print(tree.in_order())
    print("++++++++ post order +++++++++")
    print(tree.post_order())

    bTree = BinarySearchTree()
    bTree.add(23)
    bTree.add(8)
    bTree.add(42)
    bTree.add(4)
    print(bTree.pre_order())
    print(bTree.contains(4))
