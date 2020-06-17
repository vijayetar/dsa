def sort_insertion(arr):
    ''' function to do sort insertion of an array using temp variable '''
    for i in range(len(arr)):
        j = i - 1
        temp = arr[i]
        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
    return arr

def sort_insertion1(arr):
    ''' function doing sort insertion without temp, but swapping values '''
    for i in range(len(arr)):
        j = i - 1
        while j>=0 and arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j = j-1
    return arr
if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    arr1 = [20,18,12,8,5,-2]
    arr2 = [5,12,7,5,5,7]
    arr3 = [2,3,5,7,13,11]
    print(sort_insertion(arr3))
