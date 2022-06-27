import pytest
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue


# Enqueue in the pseudo queue
def test_enqueue(pseudo_enqueue):
    actual = pseudo_enqueue
    expected = "-20"
    assert actual == expected


@pytest.fixture()
def pseudo_enqueue():
    pseudo = PseudoQueue()
    pseudo.enqueue(20)
    return pseudo.__str__()


# Enqueue multiple elements in the pseudo queue
def test_enqueue_multiple(pseudo_enqueue_multiple):
    actual = pseudo_enqueue_multiple
    expected = "-10-15-20"
    assert actual == expected


@pytest.fixture()
def pseudo_enqueue_multiple():
    pseudo = PseudoQueue()
    pseudo.enqueue(20)
    pseudo.enqueue(15)
    pseudo.enqueue(10)
    return pseudo.__str__()


# Dequeue from the pseudo queue
def test_dequeue(pseudo_dequeue):
    actual = pseudo_dequeue
    expected = "-5-10-15"
    assert actual == expected


@pytest.fixture()
def pseudo_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue(20)
    pseudo.enqueue(15)
    pseudo.enqueue(10)
    pseudo.enqueue(5)
    pseudo.dequeue()
    return pseudo.__str__()

# Dequeue multiple elements from the pseudo queue
def test_dequeue_multiple(dequeue_multiple):
    actual = dequeue_multiple
    expected = "-5"
    assert actual == expected


@pytest.fixture()
def dequeue_multiple():
    pseudo = PseudoQueue()
    pseudo.enqueue(20)
    pseudo.enqueue(15)
    pseudo.enqueue(10)
    pseudo.enqueue(5)
    pseudo.dequeue()
    pseudo.dequeue()
    pseudo.dequeue()
    return pseudo.__str__()
