import pytest

from  dsa.data_structures.linked_list.linked_list import LinkedList

def test_for_in():

    foods = LinkedList()
    foods.insert("apple","banana","cucumber")
    foods_list = [food for food in foods]
    assert foods_list == ['cucumber', 'banana', 'apple']


def test_list_comprehension():

    foods = LinkedList()
    foods.insert("apple","banana","cucumber")
    cap_foods = [food.upper() for food in foods]
    assert cap_foods == ['CUCUMBER', 'BANANA', 'APPLE']

def test_list_cast():

    food_list = ['cucumber', 'banana', 'apple']
    foods = LinkedList()
    foods.insert("apple","banana","cucumber")
    assert list(foods) == food_list

def test_range():
    nums = LinkedList()
    num_range = range(1,20+1)
    print("this is num_range", num_range)
    nums.insert(num_range)
    assert len(nums) == 20


# def test_filter():

#     nums = LinkedList(range(1,21))

#     odds = [num for num in nums if num % 2]

#     assert odds == [1,3,5,7,9,11,13,15,17,19]

# def test_next():

#     foods = LinkedList(["apple","banana","cucumber"])

#     iterator = iter(foods)

#     assert next(iterator) == "apple"
#     assert next(iterator) == "banana"
#     assert next(iterator) == "cucumber"

# def test_stop_iteration():

#     foods = LinkedList(["apple","banana","cucumber"])

#     iterator = iter(foods)

#     with pytest.raises(StopIteration):
#         while True:
#             food = next(iterator)


# def test_str():
#     foods = LinkedList(["apple","banana","cucumber"])
#     assert str(foods) == "[ apple ] -> [ banana ] -> [ cucumber ] -> None"

# # dunder method tests

# def test_equals():

#     lla = LinkedList(["apple","banana","cucumber"])
#     llb = LinkedList(["apple","banana","cucumber"])

#     assert lla == llb

# def test_get_item():

#     foods = LinkedList(["apple","banana","cucumber"])

#     assert foods[0] == "apple"

# def test_get_item_out_of_range():

#     foods = LinkedList(["apple","banana","cucumber"])

#     with pytest.raises(IndexError):
#         foods[100]
