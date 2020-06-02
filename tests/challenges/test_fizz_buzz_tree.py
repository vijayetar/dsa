import pytest
from dsa.challenges.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree, BinaryTree
from dsa.data_structures.tree.tree import Node

def test_fbt_raise_error_not_tree():
    node = Node("bt")
    with pytest.raises(ValueError):
        fizz_buzz_tree(node)

def test_fbt_raise_error_no_root():
    tree = BinaryTree()
    with pytest.raises(Exception):
        fizz_buzz_tree(tree)

def test_fbt_three_nodes():
    tree = BinaryTree()
    tree.add(45)
    tree.add(10)
    tree.add(7)
    fb_tree = fizz_buzz_tree(tree)
    actual = str(fb_tree)
    expected = "FizzBuzz--> Buzz--> 7--> NULL"
    assert actual == expected

def test_fbt_multiple_nodes(bt_full):
    fb_tree = fizz_buzz_tree(bt_full)
    actual = str(fb_tree)
    expected = "FizzBuzz--> FizzBuzz--> Buzz--> Fizz--> 22--> NULL"
    assert actual == expected

#__________________________________
@pytest.fixture()
def bt_full():
    bt_full = BinaryTree()
    bt_full.add(15)
    bt_full.add(45)
    bt_full.add(27)
    bt_full.add(22)
    bt_full.add(10)
    return bt_full
