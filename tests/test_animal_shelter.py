import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter


def test_enqueue(enqueue):
    actual = enqueue
    expected = "-cat"
    assert actual == expected


@pytest.fixture()
def enqueue():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    return shelter.__str__()


def test_enqueue_multiple(enqueue_multiple):
    actual = enqueue_multiple
    expected = "-cat-dog-dog"
    assert actual == expected


@pytest.fixture()
def enqueue_multiple():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    return shelter.__str__()


def test_dequeue_dog(dequeue_dog):
    actual = dequeue_dog
    expected = "-dog-cat"
    assert actual == expected


@pytest.fixture()
def dequeue_dog():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.dequeue("dog")
    return shelter.__str__()


def test_dequeue_cat(dequeue_cat):
    actual = dequeue_cat
    expected = "-dog-dog"
    assert actual == expected


@pytest.fixture()
def dequeue_cat():
    shelter = AnimalShelter()
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.dequeue("cat")
    return shelter.__str__()


def test_dequeue_snake(dequeue_snake):
    actual = dequeue_snake
    expected = None
    assert actual == expected


@pytest.fixture()
def dequeue_snake():
    shelter = AnimalShelter()
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    return shelter.dequeue("snake")