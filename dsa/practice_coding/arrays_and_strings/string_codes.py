# 1.1 create a string of unique charcaters
def string_unique(the_string):
    if len(the_string)>256:
        return False
    chr_set = {}
    for chr in the_string:
        if chr in chr_set:
            return False
        chr_set[chr] = True
    return True

#1.2 check if two strings are permutations of each other
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

#1.3 URLify: method to replace all spaces with %20
def urlify_string(the_string):
    new_string = ''
    for chr in the_string:
        if chr==" ":
            new_string += "%20"
        else:
            new_string += chr
    return new_string

def checkpalindrone(the_list):
    if (len(the_list)%2)== 0:
        mid = len(the_list)//2
    else:
        mid = len(the_list)//2+1
    for i in range(mid):
        if the_list[i] != the_list[(i*-1)-1]:
            return False
    return True


if __name__ == "__main__":
    # the_string = "chek ing"
    # print(urlify_string(the_string))
    # string_1 = "abcdefgabcdefg"
    # string_2 = "gfedcbaabcdddg"
    # print(string_permutation(string_1, string_2))
    the_list = [1, 2]
    print(checkpalindrone(the_list))
