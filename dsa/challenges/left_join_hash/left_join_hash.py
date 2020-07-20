from dsa.challenges.hashtable.hashtable import Hashtable
from dsa.challenges.hashtable.linked_list_hashtable import LinkedList, Node

def join_hashtable(table1, table2, which_join="left"):
    '''
    Function that takes in two tables as hashmaps (dictionary) for left join and variable "right" for right join and returns mutated table
    '''
    if which_join == "left":
        to_join, table = table1, table2
    else:
        to_join, table = table2, table1
    for key in to_join:
        if not key in table:
            value = "Null"
        else:
            value = table[key]
        to_join[key]+= f", {value}"
    return to_join


if __name__ == "__main__":
    table1= {"word1":"synonym1", "word2":"synonym2", "word3":"synonym3"}
    table2 = {"word4":"antonym4", "word2":"antonym2", "word3":"antonym3"}
    print(join_hashtable(table1, table2, "right"))
