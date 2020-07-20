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


def test_filter():

    nums = LinkedList()
    for i in range(1,21):
        nums.insert(i)
    odds = [num for num in nums if num % 2]

    assert odds == [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

def test_next():

    foods = LinkedList()
    foods.insert("apple","banana","cucumber")

    iterator = iter(foods)

    assert next(iterator) == "cucumber"
    assert next(iterator) == "banana"
    assert next(iterator) == "apple"

def test_stop_iteration():

    foods = LinkedList()
    foods.insert("apple","banana","cucumber")

    iterator = iter(foods)

    with pytest.raises(StopIteration):
        while True:
            food = next(iterator)


def test_str():
    foods = LinkedList()
    foods.insert("apple","banana","cucumber")
    assert str(foods) == "{cucumber} -> {banana} -> {apple} ->  NULL"

# dunder method tests

def test_equals():

    lla = LinkedList()
    lla.insert("apple","banana","cucumber")
    llb = LinkedList()
    llb.insert("apple","banana","cucumber")

    assert len(lla) == len(llb)
    assert str(lla)==str(llb)

# def test_get_item():
#     lla = LinkedList()
#     lla.insert("apple","banana","cucumber")
#     lla = iter(lla)
#     assert lla[0] == "cucumber"

# def test_get_item_out_of_range():
#     lla = LinkedList()
#     lla.insert("apple","banana","cucumber")

#     with pytest.raises(IndexError):
#         lla[100]
