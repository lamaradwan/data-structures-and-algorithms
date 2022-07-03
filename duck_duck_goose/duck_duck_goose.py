from stack_and_queue.stack_and_queue import Queue


# args = [A,B,C,D,E]
def duck_duck_goose(k, *args):
    queue = Queue()
    counter = 1
    for i in args:
        queue.enqueue(i)
    while queue.front.next:
        if counter != k:
            queue.enqueue(queue.dequeue())
            counter += 1
        else:
            queue.dequeue()
            counter = 1
    return queue.front.value


if __name__ == "__main__":
    print("Hi")
    print(duck_duck_goose(2, "A","B","C","D","E"))
