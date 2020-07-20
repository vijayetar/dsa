# create a string of unique charcaters
def string_unique(the_string):
    if len(the_string)>256:
        return False
    chr_set = {}
    for chr in the_string:
        if chr in chr_set:
            return False
        chr_set[chr] = True
    return True

#check if two strings are permutations of each other
def string_permutation(string_1, string_2):
    if not len(string_1) == len(string_2):
        return False
    char_set = {}
    for char in string_1:
        if not char in char_set:
            char_set[char]=1
        else:
            char_set[char]+=1
    for char in string_2:
        if not char in char_set:
            return False
        else:
            char_set[char]-=1
            if char_set[char]<0:
                return False
            elif char_set[char]==0:
                del char_set[char]
    return char_set=={}



if __name__ == "__main__":
    the_string = "cheking"
    # print(string_unique(the_string))
    string_1 = "abcdefgabcdefg"
    string_2 = "gfedcbaabcdddg"
    print(string_permutation(string_1, string_2))
