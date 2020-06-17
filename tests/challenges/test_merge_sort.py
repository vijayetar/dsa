import pytest
from dsa.challenges.merge_sort.merge_sort import merge_sort

def test_merge_sort():
    assert merge_sort([1])

def test_merge_sort_empty_array():
    actual = merge_sort([])
    expected = []
    assert actual == expected

def test_merge_sort_one_array():
    actual = merge_sort([1])
    expected = [1]
    assert actual == expected

def test_merge_sort_two_array():
    actual = merge_sort([8,4])
    expected = [4,8]
    assert actual == expected

def test_merge_sort_variable_array():
    actual = merge_sort([8,4,23,42,16,15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_merge_sort_reverse_sorted_array():
    actual = merge_sort([20,18,12,8,5,-2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_merge_sort_few_uniques_array():
    actual = merge_sort([5,12,7,5,5,7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_merge_sort_nearly_sorted_array():
    actual = merge_sort([2,3,5,7,13,11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
