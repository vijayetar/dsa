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
    actual = str(bst)
    expected = "NULL"
    assert actual == expected

def test_BT_add_root():
    bt = BinaryTree()
    bt.add("44")
    actual = str(bt)
    expected = "44--> NULL"
    assert actual == expected

def test_BT_add_to_root(bt_full):
    actual= str(bt_full)
    expected = "44--> apples--> bananas--> 120--> 100--> kiwi--> NULL"
    assert actual == expected

def test_BT_preOrder(bt_full):
    actual = bt_full.preOrder()
    expected = ['44', 'apples', 'bananas', 120, 100, 'kiwi']
    assert actual == expected

def test_BT_inOrder(bt_full):
    actual = bt_full.inOrder()
    expected = ['bananas', 'apples', 120, '44', 'kiwi', 100]
    assert actual == expected

def test_BT_postOrder(bt_full):
    actual = bt_full.postOrder()
    expected = ['bananas', 120, 'apples', 'kiwi', 100, '44']
    assert actual == expected

def test_BST_add_nonInteger():
    bst=BinarySearchTree()
    actual = bst.add('apple')
    expected = "Binary Search Tree can only take integers"
    assert actual == expected

def test_BST_add_to_root(bst_full):
    actual = str(bst_full)
    expected = "15--> 8--> 3--> 5--> 65--> NULL"
    assert actual == expected

def test_BST_contains_nonInteger():
    bst = BinarySearchTree()
    actual = bst.contains("apples")
    expected = "Binary Search Tree contains only take integers"
    assert actual == expected

def test_BST_contains_empty_tree():
    bst = BinarySearchTree()
    actual = bst.contains(44)
    expected = "Binary Search Tree is empty"
    assert actual == expected

def test_BST_contains_true_value(bst_full):
    actual = bst_full.contains(5)
    expected = True
    assert actual == expected

def test_BST_contains_false_value(bst_full):
    actual = bst_full.contains(58)
    expected = False
    assert actual == expected


#_____________________________________________
@pytest.fixture()
def bst_full():
    bst_full = BinarySearchTree()
    bst_full.add(15)
    bst_full.add(8)
    bst_full.add(3)
    bst_full.add(5)
    bst_full.add(65)
    return bst_full

@pytest.fixture()
def bt_full():
    bt = BinaryTree()
    bt.add("44")
    bt.add("apples")
    bt.add(100)
    bt.add("bananas")
    bt.add(120)
    bt.add("kiwi")
    return bt