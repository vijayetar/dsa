import pytest
from dsa.challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter

def test_animalshelter_import():
    assert AnimalShelter()

def test_animalshelter_instantiate_empty():
    ash = AnimalShelter()
    actual = ash._dog_shelter.isEmpty() and ash._cat_shelter.isEmpty() and ash._others_shelter.isEmpty()
    expected = True
    assert actual == expected

def test_animalshelter_enqueue_dog():
    ash = AnimalShelter()
    ash.enqueue("dog", "Lucky")
    actual = str(ash._dog_shelter)
    expected = "{Lucky} -> NULL"
    assert actual == expected

def test_animalshelter_enqueue_cat():
    ash = AnimalShelter()
    ash.enqueue("cat", "Queen")
    actual = str(ash._cat_shelter)
    expected = "{Queen} -> NULL"
    assert actual == expected

def test_animalshelter_enqueue_other():
    ash = AnimalShelter()
    ash.enqueue("rabbit", "Jo")
    actual = str(ash._others_shelter)
    expected = "{rabbit-Jo} -> NULL"
    assert actual == expected

def test_animalshelter_dequeue_cat(ash):
    actual = ash.dequeue("cat")
    expected = "Queen"
    assert actual == expected

def test_animalshelter_dequeue_dog(ash):
    actual = ash.dequeue("dog")
    expected = "Lucky"
    assert actual == expected

def test_animalshelter_dequeue_others(ash):
    actual = ash.dequeue("others")
    expected = "rabbit-Jo"
    assert actual == expected

def test_animalshelter_isEmpty_True():
    ash = AnimalShelter()
    actual = ash.isEmpty()
    expected = True
    assert actual == expected

def test_animalshelter_isEmpty_False(ash):
    actual = ash.isEmpty()
    expected = False
    assert actual == expected

def test_animalshelter_string_full_shelter(ash):
    actual = str(ash)
    expected = "DOGS: {Lucky} -> {Happy} -> NULL CATS: {Queen} -> {Jack} -> NULL OTHERS: {rabbit-Jo} -> {snake-King} -> NULL "
    assert actual == expected

def test_animalshelter_peek_cat(ash):
    actual = ash.peek("cat")
    expected = "Queen"
    assert actual == expected

def test_animalshelter_peek_dog(ash):
    actual = ash.peek("dog")
    expected = "Lucky"
    assert actual == expected

def test_animalshelter_peek_other(ash):
    actual = ash.peek("other")
    expected = "rabbit-Jo"
    assert actual == expected

#------------------
@pytest.fixture()
def ash():
    ash = AnimalShelter()
    ash.enqueue("dog", "Lucky")
    ash.enqueue("cat", "Queen")
    ash.enqueue("rabbit", "Jo")
    ash.enqueue("dog", "Happy")
    ash.enqueue("cat", "Jack")
    ash.enqueue("snake", "King")
    return ash
