from dsa.challenges.hashtable.hashtable import Hashtable

def test_Hashtable_import():
    assert Hashtable

def test_Hashtable_empty():
    test = Hashtable(10)
    actual = str(test)
    expected = 'None'
    assert actual == expected

def test_Hashtable_hash():
    test = Hashtable(10)
    actual = test.hash("test")
    expected = 2
    assert actual == expected

def test_Hashtable_add():
    test = Hashtable(10)
    test.add("my",30)
    actual = str(test)
    expected = str(["my", 30])
    assert actual == expected

def test_Hashtable_get():
    test = Hashtable(10)
    test.add('my', 45)
    actual = str(test.get('my'))
    expected = str(45)
    assert actual == expected

def test_Hashtable_contains():
    test = Hashtable(10)
    test.add('my', 45)
    actual = test.contains('my')
    expected = True
    assert actual == expected

def test_Hashtable_collision():
    test = Hashtable(10)
    test.add('my', 45)
    test.add('ym', 25)
    actual = test.contains('my')
    expected = True
    assert actual == expected

def test_Hashtable_collision_get():
    test = Hashtable(10)
    test.add('my', 45)
    test.add('ym', 25)
    actual = str(test.get("ym"))
    expected = str(25)
    assert actual == expected

