# import pytest
# from dsa.challenges.ll_merge.ll_merge import merge_list
# from dsa.data_structures.linked_list.linked_list import Node, LinkedList

# def test_merge_lists_same_length():
#     ll1 = LinkedList()
#     ll2 = LinkedList()
#     ll1.insert("a","b","c")
#     ll2.insert("A","B","C")
#     actual = merge_list(ll1, ll2)
#     expected = 'c : C : b : B : a : A : None'
#     assert actual == expected

# def test_merge_list_link1_long():
#     ll1 = LinkedList()
#     ll2 = LinkedList()
#     ll1.insert("a","b","c","d","e","f")
#     ll2.insert("A","B","C")
#     actual = merge_list(ll1, ll2)
#     expected = "f : C : e : B : d : A : c : b : a : None"
#     assert actual == expected

# def test_merge_list_link2_long():
#     ll1 = LinkedList()
#     ll2 = LinkedList()
#     ll1.insert("a","b","c")
#     ll2.insert("A","B","C","D","E","F")
#     actual = merge_list(ll1, ll2)
#     expected = "c : F : b : E : a : D : C : B : A : None"
#     assert actual == expected

# def test_merge_list_link1_head():
#     ll1 = LinkedList()
#     ll2 = LinkedList()
#     ll2.insert("A","B","C")
#     actual = merge_list(ll1, ll2)
#     expected = "C : B : A : None"
#     assert actual == expected

# def test_merge_list_link2_head():
#     ll1 = LinkedList()
#     ll2 = LinkedList()
#     ll1.insert("a","b","c","d","e","f")
#     actual = merge_list(ll1, ll2)
#     expected = "f : e : d : c : b : a : None"
#     assert actual == expected
