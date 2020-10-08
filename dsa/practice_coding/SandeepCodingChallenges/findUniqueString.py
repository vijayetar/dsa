#----------------------------------------
# return boolean if string has unique characters or not

def ifUnique(newString):
    char_dict= {}
    for char in newString:
        if (char not in char_dict):
            char_dict[char]=1
        else:
            return False
    return True

#----------------------------------------
# modify the solution to give all the non-unique characters in a string
# abcdeeffgg => efg
def allUniqueCharacters(newString):
    char_dict= {}
    setOfChar = set()
    for char in newString:
        if (char not in char_dict):
            char_dict[char]=1
        else:
            setOfChar.add(char)
    return setOfChar
# space = O(n), time = O(n)

#----------------------------------------
# Given a sentence, return the frequency of each word that appears (hashmap question)

def writeFrequencyOfWord(newSentence):
    # breakup the words into an array
    word_array = newSentence.split(" ")
    word_dict = {}
    for word in word_array:
        if (word not in word_dict):
            word_dict[word]=1
        else:
            word_dict[word]+=1
    for k,v in enumerate(word_dict):
        print(k,v,word_dict[v])

# space = O(n), time = O(n)
#----------------------------------------
# Given a Knight and a target piece on a chess board, find out the minimum number of hops required to reach the target






#----------------------------------------
if __name__ == "__main__":
    # print(ifUnique("tesing1"))
    # print(allUniqueCharacters("testing1test"))
    print(writeFrequencyOfWord("this is the sentence is the sentence Swamishree SwamiNarayan Swamishree"))
