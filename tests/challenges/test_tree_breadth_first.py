import pytest
from dsa.challenges.tree_breadth_first.tree_breadth_first import BinaryTree

def test_BT_import():
    assert BinaryTree()

def test_BT_breadth_first_empty_tree():
    bt = BinaryTree()
    actual = bt.breadth_first()
    expected = 'NULL'
    assert actual == expected

def test_BT_breadth_first_three_nodes_tree():
    bt = BinaryTree()
    bt.add("apples")
    bt.add("kiwi")
    bt.add("bananas")
    actual = bt.breadth_first()
    expected = ['apples', 'kiwi', 'bananas']
    assert actual == expected

def test_BT_breadth_first_seven_nodes_tree():
    bt = BinaryTree()
    bt.add("apples")
    bt.add("kiwi")
    bt.add("bananas")
    bt.add("1")
    bt.add("3")
    bt.add("5")
    bt.add("7")
    actual = bt.breadth_first()
    expected = ['apples', 'kiwi', 'bananas', '1', '3', '5', '7']
    assert actual == expected
