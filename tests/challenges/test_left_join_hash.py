from dsa.challenges.left_join_hash.left_join_hash import join_hashtable

def test_left_join():
    table1= {"word1":"synonym1", "word2":"synonym2", "word3":"synonym3"}
    table2 = {"word4":"antonym4", "word2":"antonym2", "word3":"antonym3"}
    actual = join_hashtable(table1, table2, "left")
    expected = {'word1': 'synonym1, Null','word2': 'synonym2, antonym2','word3': 'synonym3, antonym3',}
    assert actual == expected

def test_right_join():
    table1= {"word1":"synonym1", "word2":"synonym2", "word3":"synonym3"}
    table2 = {"word4":"antonym4", "word2":"antonym2", "word3":"antonym3"}
    actual = join_hashtable(table1, table2,"right")
    expected ={'word2': 'antonym2, synonym2','word3': 'antonym3, synonym3','word4': 'antonym4, Null',}
    assert actual == expected
