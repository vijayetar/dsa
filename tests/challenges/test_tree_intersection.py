import pytest
from dsa.challenges.tree_intersection.tree_intersection import find_intersection
from dsa.data_structures.tree.tree import BinaryTree2

def test_find_intersection_empty_trees():
    bt1 = BinaryTree2()
    bt2 = BinaryTree2()
    with pytest.raises(ValueError):
        find_intersection(bt1, bt2)

def test_find_intersection_one_empty_tree(bt_tree):
    bt2 = BinaryTree2()
    with pytest.raises(Exception):
        find_intersection(bt_tree, bt2)

def test_find_intersection_two_small_trees(bt_trees_equal):
    bt1, bt2 = bt_trees_equal
    actual = find_intersection(bt1, bt2)
    expected = [15, 45, 22, 10, 27]
    assert actual == expected

def test_find_intersection_two_unequal_trees(bt_trees_unequal):
    bt1, bt2 = bt_trees_unequal
    actual = find_intersection(bt1, bt2)
    expected = [15, 45]
    assert actual == expected

@pytest.fixture()
def bt_tree():
    bt_full = BinaryTree2()
    bt_full.add(15)
    bt_full.add(45)
    bt_full.add(27)
    bt_full.add(22)
    bt_full.add(10)
    return bt_full

@pytest.fixture()
def bt_trees_equal():
    bt1 = BinaryTree2()
    bt1.add(15)
    bt1.add(45)
    bt1.add(27)
    bt1.add(22)
    bt1.add(10)
    bt2 = BinaryTree2()
    bt2.add(15)
    bt2.add(45)
    bt2.add(27)
    bt2.add(22)
    bt2.add(10)
    return (bt1, bt2)

@pytest.fixture()
def bt_trees_unequal():
    bt1 = BinaryTree2()
    bt1.add(15)
    bt1.add(45)
    bt2 = BinaryTree2()
    bt2.add(15)
    bt2.add(45)
    bt2.add(27)
    bt2.add(22)
    bt2.add(10)
    return (bt1, bt2)
