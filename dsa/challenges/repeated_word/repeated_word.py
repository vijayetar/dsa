import re

def repeated_word(phrase):
    '''
    function that takes in argument string and then return the first repeated word
    '''
    if not phrase:
        raise Exception("This is an Empty String")
    word_dict = {}
    word_list = re.findall(r"\w[a-zA-Z]*", phrase)
    for word in word_list:
        if word.lower() not in word_dict:
            word_dict[word.lower()]= None
        else:
            return word

def repeated_word_count(phrase):
    '''
    function that takes in argument string and then return a dictionary with all the words and the frequencies
    '''
    if not phrase:
        raise Exception("This is an Empty String")
    word_dict = {}
    word_list = re.findall(r"\w[a-zA-Z]*", phrase)
    for word in word_list:
        if word.lower() not in word_dict:
            word_dict[word.lower()]= 0
        else:
            word_dict[word.lower()]+= 1
    return word_dict

def repeated_word_list_array(phrase):
    '''
    function that takes in argument string and then return a list of most common words and the count
    '''
    word_dict = repeated_word_count(phrase)
    word_kv_array = list(word_dict.items())
    quick_sort(word_kv_array)
    return word_kv_array


def repeated_word_list_words(phrase):
    '''
    function that takes in argument string and then return a list of the most common words
    '''
    word_kv_array = repeated_word_list_array(phrase)
    print(word_kv_array)
    word_array=[]
    for i in range((len(word_kv_array)-1),-1,-1):
        word_array.append(word_kv_array[i][0])
    return word_array


def repeated_word_most_common(phrase):
    '''
    function that takes in argument string and then return most common word
    '''
    word_kv_array = repeated_word_list_array(phrase)
    return word_kv_array.pop(len(word_kv_array)-1)[0]

def quick_sort(arr, left=0, right=None):
    if right == None:
        right = len(arr)-1
    if left < right:
        pos = partition(arr,left,right)
        quick_sort(arr, left, pos-1)
        quick_sort(arr, pos+1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[right][1]
    low = left-1
    # iterate over left to the pivot-1
    for i in range(left,right):
        if arr[i][1]<= pivot:
            low = low + 1
            swap(arr, i, low)
    swap(arr, right, low+1)
    return low+1

def swap(arr, i, low):
    arr[i], arr[low] = arr[low], arr[i]
    return

if __name__ == "__main__":
    print(repeated_word_list_words("Once upon a time, there was a brave princess who..."))
