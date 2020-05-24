import pytest

from dsa.data_structures.stack_and_queues.stack_and_queues import Node, Stack

def test_check_stack():
    assert Stack

def test_check_node():
    assert Node

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

