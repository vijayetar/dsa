import pytest

from dsa.data_structures.tree.tree import Node, BinaryTree, BinarySearchTree

def test_Node_import():
    Node("value")

def test_BT_import():
    BinaryTree()

def test_BST_import():
    BinarySearchTree()

def test_BT_instantiation():
    bt = BinaryTree()
    actual = str(bt)
    expected = "NULL"
    assert actual == expected

def test_BST_instantiation():
    bst = BinarySearchTree()
    actual = bst.root
    expected = None
    assert actual == expected

def test_BT_add_to_root():
    bt = BinaryTree()
    bt.add("44")
    actual = str(bt)
    expected = "44"
    assert actual == expected

def test_BST_add_to_root():
    bst = BinarySearchTree()
    bst.add("44")
    actual = str(bst)
    expected = "44"
    assert actual == expected
