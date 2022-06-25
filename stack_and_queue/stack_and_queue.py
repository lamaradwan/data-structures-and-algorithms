class EmptyStackException(Exception):
    pass


class EmptyQueueException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if not self.top:
            raise EmptyStackException("The stack is empty, You can't pop from")

        temp_node = self.top
        self.top = self.top.next
        temp_node.next = None
        return temp_node.value

    def peek(self):
        if not self.top:
            raise EmptyStackException("The stack is empty you cant peek")

        return self.top.value

    def isEmpty(self):
        if not self.top:
            return True
        else:
            return False

    def __str__(self):
        current = self.top
        items = ''

        if not current:
            return "Empty Stack"

        while current:
            items = items + "-" + str(current.value)
            current = current.next

        return items


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.front == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if not self.front:
            raise EmptyQueueException("Empty Queue, you can't dequeue from")
        else:
            temp_node = self.front
            self.front = self.front.next
            return temp_node.value

    def peek(self):
        if not self.front:
            raise EmptyQueueException("Empty Queue, you' can't peek")
        else:
            return self.front.value

    def isEmpty(self):
        if not self.front:
            return True
        else:
            return False

    def __str__(self):
        current = self.front
        strQueue = ''

        if not current:
            return "Empty Queue"

        while current:
            strQueue = strQueue + "-" + str(current.value)
            current = current.next
        return strQueue


if __name__ == '__main__':
    # **************** Stack  ****************
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # stack.push(5)
    # print(stack.pop())
    # print(stack)
    # print(stack.peek())
    # print(stack.isEmpty())

    # ****************  Queue  ****************
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)
    queue.enqueue(11)
    queue.enqueue(13)
    print(queue)
    # print(queue.dequeue())
    # print(queue)
    # print(f"Front is {queue.front.value}")
    # print(f"Rear is {queue.rear.value}")
    # print(queue.peek())
    # print(queue.isEmpty())
