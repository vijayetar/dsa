import pytest

from dsa.data_structures.stack_and_queues.stack_and_queues import Node, Stack, Queue, QueueDeque

def test_check_stack():
    assert Stack

def test_check_node():
    assert Node

def test_check_queue():
    assert Queue

def test_check_queue_deque():
    assert QueueDeque

#Stack tests
def test_Stack_instantiate_empty_stack():
    fruits = Stack()
    actual = str(fruits)
    expected = "NULL"
    assert actual == expected

#check error raised with pop
def test_Stack_pop_raiseError(empty_stack):
    with pytest.raises(Exception):
        empty_stack.pop()

#check error raised with peek
def test_Stack_peek_raiseError(empty_stack):
    with pytest.raises(Exception):
        empty_stack.peek()

def test_Stack_push_newValue():
    fruit = Stack()
    fruit.push("apples")
    actual = str(fruit)
    expected = "{apples} -> NULL"
    assert actual == expected

def test_Stack_pop(fruit_stack):
    actual = fruit_stack.pop()
    expected = "bananas"
    assert actual == expected

def test_Stack_push_multipleValues(fruit_stack):
    fruit_stack.push("1","2","3")
    actual = str(fruit_stack)
    expected = "{3} -> {2} -> {1} -> {bananas} -> {apples} -> NULL"
    assert actual == expected

# Queue tests
def test_Queue_instantiate_empty_queue():
    my_queue = Queue()
    actual = str(my_queue)
    expected = "NULL"
    assert actual == expected

def test_Queue_peek_raiseError():
    my_queue = Queue()
    with pytest.raises(Exception):
        my_queue.peek()

def test_Queue_isEmpty_empty_queue():
    my_queue = Queue()
    actual = my_queue.isEmpty()
    expected = True
    assert actual == expected

def test_Queue_isEmpty_full_queue(full_queue):
    actual = full_queue.isEmpty()
    expected = False
    assert actual == expected

def test_Queue_peek_full_queue(full_queue):
    actual = full_queue.peek()
    expected = "task1"
    assert actual == expected

def test_Queue_enqueue_empty_queue():
    my_queue = Queue()
    my_queue.enqueue("task1")
    my_queue.enqueue("task2")
    my_queue.enqueue("task3")
    actual = str(my_queue)
    expected = "{task1} -> {task2} -> {task3} -> NULL"
    assert actual == expected

def test_Queue_dequeue_raiseError():
    my_queue = Queue()
    with pytest.raises(Exception):
        my_queue.dequeue()

def test_Queue_dequeue_one(full_queue):
    actual = full_queue.dequeue()
    expected = "task1"
    assert actual == expected

def test_Queue_deque_full_queue(full_queue):
    full_queue.dequeue()
    full_queue.dequeue()
    full_queue.dequeue()
    full_queue.dequeue()
    actual= full_queue.isEmpty()
    expected = True
    assert actual == expected

# def test_QueueDequeue_instantiate_empty_queue():
#     my_queue = QueueDeque()
#     actual = str(my_queue)
#     expected = "NULL"
#     assert actual == expected
#---------------------------------------
@pytest.fixture()
def empty_stack():
    empty_stack = Stack()
    return empty_stack

@pytest.fixture()
def fruit_stack():
    fruit_stack = Stack()
    fruit_stack.push("apples")
    fruit_stack.push("bananas")
    return fruit_stack

@pytest.fixture()
def full_queue():
    full_queue = Queue()
    full_queue.enqueue("task1")
    full_queue.enqueue("task2")
    full_queue.enqueue("task3")
    full_queue.enqueue("task4")
    return full_queue

