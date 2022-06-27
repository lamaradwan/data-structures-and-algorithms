from stack_and_queue.stack_and_queue import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1_enqueue = Stack()
        self.stack2_dequeue = Stack()
        self.length_stack1 = 0

    def enqueue(self, value):
        self.stack1_enqueue.push(value)
        self.length_stack1 += 1

    def dequeue(self):
        # take the stack 1 element to stack 2
        current = self.stack1_enqueue.top
        while current:
            self.stack2_dequeue.push(current.value)
            current = current.next

        # Pop from stack 2
        popping = self.stack2_dequeue.pop()

        # Make the stack 1 empty
        for i in range(self.length_stack1):
            self.stack1_enqueue.pop()
            # print("end")

        # Push the elements in stack 2 into 1 to reorder the elements
        current2 = self.stack2_dequeue.top
        while current2:
            self.stack1_enqueue.push(current2.value)
            current2 = current2.next

        # make stack 2 empty for the next use
        for i in range(self.length_stack1 - 1):
            self.stack2_dequeue.pop()
            # print("end")

        self.length_stack1 -= 1
        return popping

    def __str__(self):
        current = self.stack1_enqueue.top
        items = ''

        if not current:
            return "Empty Stack"

        while current:
            items = items + "-" + str(current.value)
            current = current.next

        return items


if __name__ == "__main__":
    print("Hi")
    pseudo_q = PseudoQueue()
    pseudo_q.enqueue(20)
    pseudo_q.enqueue(15)
    pseudo_q.enqueue(10)
    pseudo_q.enqueue(5)
    pseudo_q.enqueue(0)
    print(pseudo_q)
    print(pseudo_q.dequeue())
    print(pseudo_q)
    pseudo_q.enqueue(200)
    print(pseudo_q)
    print(pseudo_q.dequeue())
    print(pseudo_q)
    print(pseudo_q.dequeue())
    print(pseudo_q)
