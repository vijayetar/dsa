#  find the average of continuous subarrays of size k
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

# find the max sum of the continous subarays of the size k
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








if __name__ == "__main__":
    print(getAverage([1,2,3,4,5], 2))
    print(findMaxSum([-1,-2,-3,-4,5], 3))

