import pytest

from ...dsa.data_structures.linked_list.linked_list import Node

# check Node instantiation
def test_node_instantiation():
    apples = Node("apples")
    actual = apples.value
    expected = 'apples'
    assert expected == actual

# check Node __str__
def test_node_str ():
    bananas = Node("bananas")
    actual = bananas.__str__()
    expected = "This is bananas instantiated in Node class"
    assert expected == actual

# check Node __str__
def test_node_repr ():
    bananas = Node("bananas")
    actual = bananas.__repr__()
    expected = "bananas"
    assert expected == actual

