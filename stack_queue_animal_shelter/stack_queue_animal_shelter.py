from stack_and_queue.stack_and_queue import Stack


class Animal:
    def __init__(self, pref):
        self.pref = pref
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Animal(data)
        if self.front == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self, pref):
        if pref == "cat" or pref == "dog":
            if self.rear == self.front:
                return "Now it's empty", self.rear.pref

            temp_node = self.front
            stack = Stack()
            while pref != temp_node.pref:
                # print("push to stack")
                stack.push(temp_node.pref)
                temp_node = temp_node.next
                self.front = self.front.next

            the_wanted_animal = temp_node.pref
            temp_node = temp_node.next

            while temp_node.next is not None:
                # print("continue push to stack")
                stack.push(temp_node.pref)
                temp_node = temp_node.next
                self.front = self.front.next
        else:
            return None

        # stack.push(self.front.pref)
        self.front = self.front.next
        stack.push(self.front.pref)


        while stack.top is not None:
            # print("enqueue again")
            self.enqueue(stack.top.value)
            stack.top = stack.top.next

        self.front = self.front.next
        return the_wanted_animal, stack.__str__()

    def __str__(self):
        current = self.front
        strQueue = ''

        if not current:
            return "Empty Queue"

        while current:
            strQueue = strQueue + "-" + str(current.pref)
            current = current.next
        return strQueue


if __name__ == "__main__":
    # print("Hi")
    vet = AnimalShelter()
    vet.enqueue("cat")
    vet.enqueue("dog")
    vet.enqueue("dog")
    vet.enqueue("cat")
    vet.enqueue("dog")
    print(vet)
    # print(vet.dequeue("dog2"))
    print(vet.dequeue("dog"))
    vet.enqueue("Lama")
    print(vet.dequeue("dog"))
    print(vet.dequeue("snake"))


    # print(vet.dequeue("dog"))
    # print(vet.dequeue("cat"))
    # print(vet.dequeue("cat"))
    # print(vet.dequeue("dog"))






    # print(vet.dequeue("cat2"))
    print(vet)
