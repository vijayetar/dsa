def quick_sort(arr, left, right):
    if left < right:
        pos = partition(arr,left,right)
        print('this is position', pos)
        quick_sort(arr, left, pos-1)
        quick_sort(arr, pos+1, right)

def partition(arr, left, right):
    pivot = arr[right-1]
    low = left -1
    for i in range(left,right):
        if arr[i]<= pivot:
            low = low + 1
            arr = swap(arr, i, low)
    swap(arr, right, low+1)
    return low+1

def swap(arr, i, low):
    arr[low], arr[i] = arr[i], arr[low]
    return arr

if __name__ == "__main__":
    arr = [4,3,1,6,5,2]
    print(quick_sort(arr, 0, len(arr)))
