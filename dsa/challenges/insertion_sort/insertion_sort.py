def sort_insertion(arr):
    for i in range(len(arr)):
        j = i - 1
        temp = arr[i]
        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
    return arr
if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    arr1 = [20,18,12,8,5,-2]
    arr2 = [5,12,7,5,5,7]
    arr3 = [2,3,5,7,13,11]
    print(sort_insertion(arr3))
