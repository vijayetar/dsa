#2.1
def pair_with_targetsum(arr, target_sum):
    start_index = 0
    end_index = len(arr)-1

    while(arr[start_index]!=arr[end_index]):
        sum = arr[start_index]+arr[end_index]
        if sum==target_sum:
            return [start_index, end_index]
        elif (sum<target_sum):
            start_index+=1
        else:
            end_index-=1
    return [-1,-1]


##2.2 Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

def remove_duplicates(arr):
    length = len(arr)
    i = 0
    while i<length-1:
        if arr[i]==arr[i+1]:
            arr.pop(i+1)
            length-=1
        else:
            i+=1
    return arr

#2.3 start with two pointers at the ends and then add it to the the squares based on which is bigger, and the move the pointer inwards to the middle
def make_squares(arr):
  squares = []
  end_index = len(arr)-1
  start_index = 0
  while end_index != start_index:
    if arr[end_index]**2 > arr[start_index]**2:
        squares.insert(0,arr[end_index]**2)
        end_index-=1
    else:
        squares.insert(0,arr[start_index]**2)
        start_index+=1
  squares.insert(0,arr[start_index]**2)
  return squares

#2.4 Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

def dutch_flag_sort(arr):
    start=0
    end = len(arr)-1
    i=0
    while i >end:
        if arr[i]==0:
            arr[i], arr[start]=arr[start], arr[i]
            i+=1
            start+=1
        elif arr[i]==1:
            i+=1
        else:
            arr[end], arr[i]=arr[i], arr[end]
            end -=1
    return arr


if __name__ == "__main__":
    # print(pair_with_targetsum([1,2,3,4,6,11,100],19))
    # print(remove_duplicates([1,3,3,4,5,5,5,7,7]))
    # print(make_squares([-2, -1, 0, 2, 3]))
    print(dutch_flag_sort([1,0,1,0,2,2,1,0]))
