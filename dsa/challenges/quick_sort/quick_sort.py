def quick_sort(arr, left=0, right=None):
    if right == None:
        right = len(arr)-1
    if left < right:
        pos = partition(arr,left,right)
        quick_sort(arr, left, pos-1)
        quick_sort(arr, pos+1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    low = left-1
    # iterate over left to the pivot-1
    for i in range(left,right):
        if arr[i]<= pivot:
            low = low + 1
            swap(arr, i, low)
    swap(arr, right, low+1)
    return low+1

def swap(arr, i, low):
    arr[i], arr[low] = arr[low], arr[i]
    return

if __name__ == "__main__":
    arr = [5,12,7,5,5,7]
    print(quick_sort(arr))
