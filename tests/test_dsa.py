from dsa import __version__
from dsa.challenges.array_sum_of_matrix.array_sum_of_matrix import sum_of_matrix_array

def test_version():
    assert __version__ == '0.1.0'

def test_som1():
    actual = sum_of_matrix_array([])
    expected = 'incorrect input'
    assert expected == actual

def test_som2():
    actual = sum_of_matrix_array([[1,2,3],[2,3,4],[3,4,5]])
    expected = [6,9,12]
    assert expected == actual

def test_som3():
    actual = sum_of_matrix_array([[1,"",3],[2,3,""],["",4,5]])
    expected = [4,5,9]
    assert expected == actual

def test_som4():
    actual = sum_of_matrix_array([[-1,1,-3],[2,-3,1],[1,4,-5]])
    expected = [-3,0,0]
    assert expected == actual
