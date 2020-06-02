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


#__________________________________
@pytest.fixture()
def bt_full():
    bt_full = BinaryTree()
    bt_full.add(15)
    bt_full.add(8)
    bt_full.add(3)
    bt_full.add(5)
    bt_full.add(65)
    return bt_full
