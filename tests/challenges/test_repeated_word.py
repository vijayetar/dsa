import pytest
from dsa.challenges.repeated_word.repeated_word import repeated_word, repeated_word_count, repeated_word_most_common, repeated_word_list_words

def test_repeated_word_simple():
    actual = repeated_word("this is simply simple is")
    expected = "is"
    assert actual == expected

def test_repeated_word_complex():
    actual = repeated_word("Once upon a time, there was a brave princess who...")
    expected = "a"
    assert actual == expected

def test_repeated_word_long():
    actual = repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    expected = "it"
    assert actual == expected

def test_repeated_word_another():
    actual = repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    expected = "summer"
    assert actual == expected

def test_repeated_word_count_simple():
    actual = repeated_word_count("this is simply simple is")
    expected = {'this': 0, 'is': 1, 'simply': 0, 'simple': 0}
    assert actual == expected

def test_repeated_word_count_complex():
    actual = repeated_word_count("Once upon a time, there was a brave princess who...")
    expected = {'once': 0, 'upon': 0, 'a': 1, 'time': 0, 'there': 0, 'was': 0, 'brave': 0, 'princess': 0, 'who': 0}
    assert actual == expected

def test_repeated_word_count_another():
    actual = repeated_word_count("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York in summer...")
    expected = {'it': 0, 'was': 1, 'a': 0, 'queer': 0, 'sultry': 0, 'summer': 2, 'the': 1, 'they': 0, 'electrocuted': 0, 'rosenbergs': 0, 'and': 0, 'i': 1, 'didn': 0, 't': 0, 'know': 0, 'what': 0, 'doing': 0, 'in': 1, 'new': 0, 'york': 0}
    assert actual == expected

def test_repeated_word_most_common():
    actual = repeated_word_most_common("this is simply simple is")
    expected = "is"
    assert actual == expected

def test_repeated_word_most_common_complex():
    actual = repeated_word_most_common("Once upon a time, there was a brave princess who...")
    expected = "a"
    assert actual == expected

def test_repeated_word_most_common_another():
    actual = repeated_word_most_common("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York in summer...")
    expected = "summer"
    assert actual == expected

def test_repeated_word_list_words_simple():
    actual = repeated_word_list_words("this is simply simple is")
    expected = ['is', 'simple', 'simply', 'this']
    assert actual == expected

def test_repeated_word_list_words_complex():
    actual = repeated_word_list_words("Once upon a time, there was a brave princess who...")
    expected = ['a', 'who', 'princess', 'brave', 'was', 'there', 'time', 'upon', 'once']
    assert actual == expected
