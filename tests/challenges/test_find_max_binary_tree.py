import pytest
from dsa.challenges.find_max_binary_tree.find_max_binary_tree import Node, BinaryTree

def test_BT_import():
    assert BinaryTree

def test_BT_find_max_value_raises_exception():
    bt = BinaryTree()
    with pytest.raises(Exception):
        bt.find_max_value()

def test_BT_find_max_single_val():
    bt= BinaryTree()
    bt.add(20)
    actual = bt.find_max_value()
    expected = 20
    assert actual == expected

def test_BT_find_max_zero_val():
    bt= BinaryTree()
    bt.add(0)
    actual = bt.find_max_value()
    expected = 0
    assert actual == expected


def test_BT_find_max_two_val():
    bt= BinaryTree()
    bt.add(20)
    bt.add(25)
    actual = bt.find_max_value()
    expected = 25
    assert actual == expected

def test_BT_find_max_three_val():
    bt= BinaryTree()
    bt.add(20)
    bt.add(25)
    bt.add(50)
    actual = bt.find_max_value()
    expected = 50
    assert actual == expected

def test_BT_find_max_large_tree():
    bt= BinaryTree()
    bt.add(20)
    bt.add(25)
    bt.add(50)
    bt.add(12)
    bt.add(18)
    bt.add(21)
    bt.add(0)
    bt.add(65)
    actual = bt.find_max_value()
    expected = 65
    assert actual == expected

def test_BT_find_max_negative_tree():
    bt= BinaryTree()
    bt.add(-2)
    bt.add(-25)
    bt.add(-50)
    bt.add(-12)
    bt.add(-18)
    bt.add(-21)
    bt.add(0)
    bt.add(-65)
    actual = bt.find_max_value()
    expected = 0
    assert actual == expected
