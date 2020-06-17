from dsa.challenges.insertion_sort.insertion_sort import sort_insertion, sort_insertion1

import pytest

def test_assert_sort_insertion():
    assert sort_insertion([8,4,23,42,16,15])

def test_sort_insertion_empty_array():
    arr = []
    actual = sort_insertion(arr)
    expected = []
    assert actual == expected


def test_sort_insertion_simple_array():
    arr = [8,4,23,42,16,15]
    actual = sort_insertion(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort_insertion_negative_array():
    arr = [8,4,23,42,16,15]
    actual = sort_insertion(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort_insertion_unique_array():
    arr = [5,12,7,5,5,7]
    actual = sort_insertion(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_sort_insertion_unique_array():
    arr = [2,3,5,7,13,11]
    actual = sort_insertion(arr)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

def test_assert_sort_insertion1():
    assert sort_insertion1([8,4,23,42,16,15])

def test_sort_insertion1_empty_array():
    arr = []
    actual = sort_insertion1(arr)
    expected = []
    assert actual == expected


def test_sort_insertion1_simple_array():
    arr = [8,4,23,42,16,15]
    actual = sort_insertion1(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort_insertion1_negative_array():
    arr = [8,4,23,42,16,15]
    actual = sort_insertion1(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort_insertion1_unique_array():
    arr = [5,12,7,5,5,7]
    actual = sort_insertion1(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_sort_insertion1_unique_array():
    arr = [2,3,5,7,13,11]
    actual = sort_insertion1(arr)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
