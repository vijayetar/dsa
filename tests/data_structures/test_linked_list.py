import pytest

from ...dsa.data_structures.linked_list.linked_list import Node, LinkedList

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
    expected = "bananas : None"
    assert expected == actual

# check Node __repr__
def test_node_repr ():
    bananas = Node("bananas")
    actual = bananas.__repr__()
    expected = "bananas : None"
    assert expected == actual

# check LinkedList instantiation
def test_LinkedList_instantiation():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert actual == expected

## check insert into linked list
def test_LinkedList_insert():
    ll = LinkedList()
    ll.insert("apples")
    actual = str(ll)
    expected = "{apples} ->  NULL"
    assert actual == expected

# #check multiple inserts into linked list
def test_LinkedList_insert():
    ll = LinkedList()
    ll.insert("apples", "bananas", "coconut", "dragonfruits")
    actual = str(ll)
    expected = "{dragonfruits} -> {coconut} -> {bananas} -> {apples} ->  NULL"
    assert actual == expected

# ## check True includes in the Linked List
def test_LinkedList_includes_True():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("oranges")
    ll.insert("pineapples")
    actual = ll.includes("oranges")
    expected = True
    assert actual == expected

# ## check False includes in the Linked List
def test_LinkedList_includes_False():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("oranges")
    ll.insert("pineapples")
    actual = ll.includes("kiwi")
    expected = False
    assert actual == expected

# # # check if the error is raised with and without entering a Node

def test_Node_raiseError():
    with pytest.raises(TypeError):
        lucy = Node("Lucy")
        lucky = Node("Lucky")
        mooney = Node("Mooney","this is not a node")

#------------------------------------
# @pytest.fixture()
# def prep_LinkedList_apples():
#     ll = LinkedList()
#     ll.insert("apples")
#     return ll


