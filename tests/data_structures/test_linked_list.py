import pytest

from dsa.data_structures.linked_list.linked_list import Node, LinkedList
from dsa.challenges.ll_merge.ll_merge import merge_list

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
def test_LinkedList_insert(ll):
    actual = str(ll)
    expected = "{apples} ->  NULL"
    assert actual == expected

# # #check multiple inserts into linked list
def test_LinkedList_insert(ll):
    ll.insert("bananas", "coconut", "dragonfruits")
    actual = str(ll)
    expected = "{dragonfruits} -> {coconut} -> {bananas} -> {apples} ->  NULL"
    assert actual == expected

# # ## check True includes in the Linked List
def test_LinkedList_includes_True(ll):
    ll.insert("oranges")
    ll.insert("pineapples")
    actual = ll.includes("oranges")
    expected = True
    assert actual == expected

# # ## check False includes in the Linked List
def test_LinkedList_includes_False(ll):
    ll.insert("oranges")
    ll.insert("pineapples")
    actual = ll.includes("kiwi")
    expected = False
    assert actual == expected

# # # # check if the error is raised with and without entering a Node

def test_Node_raiseError():
    with pytest.raises(TypeError):
        lucy = Node("Lucy")
        lucky = Node("Lucky")
        mooney = Node("Mooney","this is not a node")

### check append on empty linked list
def test_LinkedList_append_empty_list():
    ll = LinkedList()
    ll.append("5")
    actual = str(ll)
    expected = "{5} ->  NULL"
    assert actual == expected

def test_LinkedList_append_empty_list():
    ll = LinkedList()
    ll.insert("1","3","2")
    ll.append("5")
    actual = str(ll)
    expected = "{2} -> {3} -> {1} -> {5} ->  NULL"
    assert actual == expected

### check insert_before function
def test_LinkedList_insert_before_empty_link():
    ll = LinkedList()
    actual = ll.insert_before("apples","oranges")
    expected = "Exception"
    assert actual == expected

def test_LinkedList_insert_before_absent_value(ll):
    ll.insert("oranges")
    coconut = Node("coconut")
    actual = ll.insert_before(coconut,"kiwi")
    expected = "Exception"
    assert actual == expected

def test_LinkedList_insert_before_present_value():
    ll = LinkedList()
    ll.insert("oranges","bananas", "coconut")
    ll.insert_before("oranges","kiwi")
    actual = str(ll)
    expected = "{coconut} -> {bananas} -> {kiwi} -> {oranges} ->  NULL"
    assert actual == expected

def test_LinkedList_insert_before_multiple_arg_just_head():
    ll=LinkedList()
    ll.insert("oranges")
    ll.insert_before("oranges","1","2","3")
    actual = str(ll)
    expected = "{3} -> {2} -> {1} -> {oranges} ->  NULL"
    assert actual == expected

def test_LinkedList_insert_before_multiple_arg_long_head():
    ll=LinkedList()
    ll.insert("oranges","kiwi","bananas","coconut")
    ll.insert_before("kiwi","1","2","3")
    actual = str(ll)
    expected = "{coconut} -> {bananas} -> {3} -> {2} -> {1} -> {kiwi} -> {oranges} ->  NULL"
    assert actual == expected

def test_kth_value_empty_list():
    ll= LinkedList()
    actual = ll.find_k_node_value(3)
    expected="Exception"
    assert actual == expected

def test_kth_value_largeKay():
    ll= LinkedList()
    ll.insert("1","2","3")
    actual = ll.find_k_node_value(15)
    expected="Exception"
    assert actual == expected

def test_kth_value_negativeKay():
    ll= LinkedList()
    ll.insert("1","2","3")
    actual = ll.find_k_node_value(-15)
    expected="Exception"
    assert actual == expected

def test_kth_value_zeroKay():
    ll= LinkedList()
    ll.insert("1","2","3")
    actual = ll.find_k_node_value(0)
    expected= '1'
    assert actual == expected

def test_kth_value_full_length():
    ll= LinkedList()
    ll.insert("1","2","3","4","5")
    actual = ll.find_k_node_value(4)
    expected= '5'
    assert actual == expected

def test_kth_value_mid_length():
    ll= LinkedList()
    ll.insert("1","2","3","4","5")
    actual = ll.find_k_node_value(2)
    expected= '3'
    assert actual == expected

def test_kth_value_one():
    ll= LinkedList()
    ll.insert("1")
    actual = ll.find_k_node_value(0)
    expected= '1'
    assert actual == expected

def test_kth_value_empty_list():
    ll= LinkedList()
    actual = ll.find_k_node_value2(3)
    expected="Exception"
    assert actual == expected

def test_kth_value_largeKay():
    ll= LinkedList()
    ll.insert("1","2","3")
    actual = ll.find_k_node_value2(15)
    expected="Exception"
    assert actual == expected

def test_kth_value_negativeKay():
    ll= LinkedList()
    ll.insert("1","2","3")
    actual = ll.find_k_node_value2(-15)
    expected="Exception"
    assert actual == expected

def test_kth_value_zeroKay():
    ll= LinkedList()
    ll.insert("1","2","3")
    actual = ll.find_k_node_value2(0)
    expected= '1'
    assert actual == expected

def test_kth_value_full_length():
    ll= LinkedList()
    ll.insert("1","2","3","4","5")
    actual = ll.find_k_node_value2(4)
    expected= '5'
    assert actual == expected

def test_kth_value_mid_length():
    ll= LinkedList()
    ll.insert("1","2","3","4","5")
    actual = ll.find_k_node_value2(2)
    expected= '3'
    assert actual == expected

def test_kth_value_one():
    ll= LinkedList()
    ll.insert("1")
    actual = ll.find_k_node_value2(0)
    expected= '1'
    assert actual == expected
#------------------------------------
@pytest.fixture()
def ll():
    ll = LinkedList()
    ll.insert("apples")
    return ll


