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


    def find_maximum(self):
        if not self.root:
            return self.root

        maxi = self.root.value
        values = []
        def _walk(root):
            # max = root.value
            if root.value > maxi:
                # return root.value
                values.append(root.value)
                # print(root.value)
            else:
                if root.left:
                    _walk(root.left)

                if root.right:
                    _walk(root.right)


        _walk(self.root)

        if len(values) == 0:
            return self.root.value
        else:
            max = values[0]
            for v in values:
                if v > max:
                    max = v
            return max

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
<<<<<<< HEAD
=======
    pass
<<<<<<< HEAD
>>>>>>> array-reverse
=======
>>>>>>> 853252e (update readme for trees)
>>>>>>> array-reverse
    # tree = BinaryTree()
    # tree.root = Node("A")
    # tree.root.left = Node("B")
    # tree.root.right = Node("C")
    # tree.root.left.left = Node("D")
    # tree.root.left.right = Node("E")
    # tree.root.right.left = Node("F")
<<<<<<< HEAD

    tree = BinaryTree()
    tree.root = Node(20)
    tree.root.left = Node(23)
    tree.root.right = Node(10)
    tree.root.left.left = Node(24)
    tree.root.left.right = Node(18)
    tree.root.right.left = Node(100)
    tree.root.right.right = Node(12)

    print("++++++++ pre order +++++++++")
    print(tree.pre_order())
    print("++++++++ in order +++++++++")
    print(tree.in_order())
    print("++++++++ post order +++++++++")
    print(tree.post_order())
    print(tree.find_maximum())

<<<<<<< HEAD
=======

>>>>>>> array-reverse
=======
    # print("++++++++ pre order +++++++++")
    # print(tree.pre_order())
    # print("++++++++ in order +++++++++")
    # print(tree.in_order())
    # print("++++++++ post order +++++++++")
    # print(tree.post_order())
    #
<<<<<<< HEAD
>>>>>>> array-reverse
=======
>>>>>>> 853252e (update readme for trees)
>>>>>>> array-reverse
    # bTree = BinarySearchTree()
    # bTree.add(23)
    # bTree.add(8)
    # bTree.add(42)
    # bTree.add(4)
    # print(bTree.pre_order())
    # print(bTree.contains(4))
