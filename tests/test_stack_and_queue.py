import pytest
from stack_and_queue.stack_and_queue import Stack, Queue


# 1 Can successfully push onto a stack
def test_push(stack_push):
    actual = stack_push
    expected = "-1"
    assert actual == expected


@pytest.fixture()
def stack_push():
    stack = Stack()
    stack.push(1)
    return stack.__str__()


# 2 Can successfully push multiple values onto a stack
def test_push_multiple(stack_push_multiple):
    actual = stack_push_multiple
    expected = "-3-2-1"
    assert actual == expected


@pytest.fixture()
def stack_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack.__str__()


# 3 Can successfully pop off the stack
def test_pop_stack(pop_stack):
    actual = pop_stack
    expected = "-3-2-1"
    assert actual == expected


@pytest.fixture()
def pop_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    return stack.__str__()


# 4 Can successfully empty a stack after multiple pops
def test_multiple_pops_empty(multiple_pop_stack_empty):
    actual = multiple_pop_stack_empty
    expected = 'Empty Stack'
    assert actual == expected


@pytest.fixture()
def multiple_pop_stack_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    return stack.__str__()


# 5 Can successfully peek the next item on the stack
def test_stack_peek(stack_peek):
    actual = stack_peek
    expected = 3
    assert actual == expected


@pytest.fixture()
def stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack.peek()


# 6 Can successfully instantiate an empty stack
def test_instantiate_empty_stack(empty_stack):
    actual = empty_stack
    expected = "Empty Stack"
    assert actual == expected


@pytest.fixture()
def empty_stack():
    stack = Stack()
    return stack.__str__()


# 7 Calling pop or peek on empty stack raises exception
def test_raise_exception_on_pop():
    stack = Stack()
    with pytest.raises(Exception) as errorMsg:
        stack.pop()
    assert (str(errorMsg.value)) == "The stack is empty, You can't pop from"


# 8 Can successfully enqueue into a queue
def test_enqueue(queue_enqueue):
    actual = queue_enqueue
    expected = "-1"
    assert actual == expected

@pytest.fixture()
def queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    return queue.__str__()


# 9 Can successfully enqueue multiple values into a queue
def test_enqueue_multiple(queue_enqueue_multiple):
    actual = queue_enqueue_multiple
    expected = "-1-2-3"
    assert actual == expected

@pytest.fixture()
def queue_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue.__str__()


# 10 Can successfully dequeue out of a queue the expected value
def test_dequeue(dequeue):
    actual = dequeue
    expected = "-2-3"
    assert actual == expected

@pytest.fixture()
def dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    return queue.__str__()


# 11 Can successfully peek into a queue, seeing the expected value
def test_queue_peek(queue_peek):
    actual = queue_peek
    expected = 1
    assert actual == expected


@pytest.fixture()
def queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue.peek()


# 12 Can successfully empty a queue after multiple dequeues
def test_empty_queue(queue_empty):
    actual = queue_empty
    expected = "Empty Queue"
    assert actual == expected

@pytest.fixture()
def queue_empty():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    return queue.__str__()


# 13 Can successfully instantiate an empty queue
def test_instantiate_empty_Queue():
    queue = Queue()
    actual = queue.__str__()
    expected = "Empty Queue"
    assert actual == expected


# 14 Calling dequeue or peek on empty queue raises exception
def test_raise_exception_on_peek_empty_queue():
    queue = Queue()
    with pytest.raises(Exception) as errorMsg:
        queue.peek()
    assert (str(errorMsg.value)) == "Empty Queue, you' can't peek"
