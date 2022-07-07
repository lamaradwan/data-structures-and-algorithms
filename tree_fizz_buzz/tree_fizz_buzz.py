class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class KAry:
    def __init__(self):
        self.root = None

    def pre_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):
            result.append(root.value)
            if root.children:
                for nodes in root.children:
                    _walk(nodes)
            return result

        return _walk(self.root)

    def fizz_buzz_tree(self):
        if not self.root:
            return None
        new_tree = self

        def _walk(root):
            if (root.value % 3 == 0 and root.value % 5 == 0) and root.value != 0:
                root.value = 'FizzBuzz'
            elif root.value % 3 == 0 and root.value != 0:
                root.value = 'Fizz'
            elif root.value % 5 == 0 and root.value != 0:
                root.value = 'Buzz'
            else:
                str(root.value)

            if root.children:
                for node in root.children:
                    _walk(node)

            return new_tree
        return _walk(new_tree.root)


if __name__ == '__main__':
    pass
    # kary = KAry()
    # kary.root = Node(3)
    # kary.root.children.append(Node(2))
    # kary.root.children.append(Node(1))
    # kary.root.children.append(Node(0))
    # kary.root.children[0].children.append(Node(4))
    # kary.root.children[0].children.append(Node(5))
    # kary.root.children[0].children.append(Node(4))
    # kary.root.children[2].children.append(Node(15))
    # print(kary.pre_order())
    # kary2 = KAry()
    # # print(kary2.fizz_buzz_tree().pre_order())
    # print(kary2.fizz_buzz_tree())
    #
    # # print(kary.pre_order())
