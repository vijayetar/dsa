# 1.1 find the average of continuous subarrays of size k
def getAverage(list, k):
    average_list = []
    ## iterate from 0 to len of list -k +1
    sum = 0
    for j in range(k):
        sum += list[j]
    average_list.append(sum/k)
    for i in range (1,len(list)-k+1):
        sum = sum+(list[i+k-1]-list[i-1])
        average_list.append(sum/k)
    return average_list

# 1.2 find the max sum of the continous subarays of the size k
def findMaxSum(list, k): #5,3
    # assign the variables
    sum = 0
    max = float('-inf')
    start = 0
    # iterate over the list len-k+1 times
    for i in range (len(list)):
        # get the sum of the first k nodes
        sum += list[i] #0,1,2,3
        if i == k-1:
            max = sum
        if i>=k:#3
            sum -= list[i-k]#0
            if sum>max:
                max = sum
    return max

# 1.3
def findShortestLength(arr, k):
    start = 0
    short = float('inf')
    sum = 0
    for i in range(len(arr)): #O(n)
        sum += arr[i]
        while sum>=k:
            short = min(short,(i-start+1))
            sum -= arr[start]
            start+=1
    return short

#1.4
def find_the_longest_substring(word, k):
    char_set = set()
    substring=""
    longest_substring=""
    for char in word:
        if char not in char_set:
            char_set.add(char)
            if len(char_set)>k:
                if len(substring)>len(longest_substring):
                    longest_substring=substring
                removed_char = substring[0]
                counter = 0
                for ch in substring:
                    if ch == removed_char:
                        counter+=1
                    else:
                        break
                substring = substring[counter::]
                char_set.remove(removed_char)
        substring+=char
    if len(char_set)<k:
        return "not enough characters"
    if len(longest_substring)<len(substring):
        longest_substring = substring
    return longest_substring


# 1.6 Given a string, find the length of the longest substring which has no repeating characters.
def non_repeat_substring(str):
    char_set=set()
    substring=""
    long_string=""
    for char in str:
        if char in char_set:
            substring=""
            char_set.clear()
        char_set.add(char)
        substring+= char
        if len(long_string)<len(substring):
            long_string = substring
    if len(long_string)<len(substring):
        long_string = substring
    return long_string

if __name__ == "__main__":
    # print(getAverage([1,2,3,4,5], 2))
    # print(findMaxSum([-1,-2,-3,-4,5], 3))
    # print(findShortestLength([1,2,3,4,5],10))
    # print(find_the_longest_substring("cbbebi", 3))
    print(non_repeat_substring("abccccccdefffffff"))

