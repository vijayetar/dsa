import pytest
from dsa.challenges.quick_sort.quick_sort import quick_sort, partition, swap

def test_import_quick_sort():
    assert quick_sort

def test_quick_sort_simple():
    actual = quick_sort([8,4,23,42,16,15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_quick_sort_reverse_sorted():
    actual = quick_sort([20,18,12,8,5,-2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_quick_sort_few_unique():
    actual = quick_sort([5,12,7,5,5,7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_quick_sort_nearly_sorted():
    actual = quick_sort([2,3,5,7,13,11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

