from dsa.challenges.decorators.decorators import fun

def test_fun_simple_txt_w_verbose():
    assert fun("Karen", verbose=True)=="hi there, Karen!!"

def test_fun_simple_txt():
    assert fun("Karen")=="Karen!!"

def test_fun_int_w_verbose():
    assert fun(20, verbose=True)=="20 is NOT enough!!"

def test_fun_int():
    assert fun(20)=="have 20 of it"

def test_fun_list_w_verbose():
    actual = fun(["lemons","honey"],verbose=True)
    assert actual == ['Please get this: 1. LEMONS', 'Please get this: 2. HONEY']

def test_fun_list():
    assert fun(["lemons","honey"])=="This 2 in the list is too much "

def test_fun_float_w_verbose():
    actual = fun(0.5,verbose=True)
    assert actual == 'this is 0.5 that needs to be converted into fraction'

def test_fun_float():
    assert fun(100.5)=="please select 100.5 wisely"
