import pytest
from dsa.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_import():
    multi_bracket_validation('string')

def test_multi_bracket_emptystring():
    actual = multi_bracket_validation("")
    expected = False
    assert actual == expected

def test_multi_bracket_true_simple():
    actual = multi_bracket_validation('abcds{}()[]')
    expected = True
    assert actual == expected

def test_multi_bracket_true_complex1():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    expected = True
    assert actual == expected

def test_multi_bracket_true_complex2():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected

def test_multi_bracket_false_simple1():
    actual = multi_bracket_validation('(](')
    expected = False
    assert actual == expected

def test_multi_bracket_false_simple2():
    actual = multi_bracket_validation('{(})')
    expected = False
    assert actual == expected

def test_multi_bracket_false_complex1():
    actual = multi_bracket_validation('{}{Code}[Fellows](()')
    expected = False
    assert actual == expected

def test_multi_bracket_no_bracket():
    actual = multi_bracket_validation('jjkjklj')
    expected = "no brackets in string"
    assert actual == expected
