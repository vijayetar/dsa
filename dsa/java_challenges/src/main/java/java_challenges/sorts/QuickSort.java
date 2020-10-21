package java_challenges.sorts;

public class QuickSort {
    public int[] quickSort(int[] arr) {
        int left = 0;
        int right = arr.length-1;
        arr = quickSort(arr, left, right);
        return arr;
    }

    public int[] quickSort(int[] arr, int left, int right) {
        if (left<right) {
            int position = partition(arr, left, right);
            arr = quickSort(arr, left, position-1);
            arr = quickSort(arr, position+1, right);
        }
        return arr;
    }
    private int[] swap(int[] arr, int low, int i){
        int temp = arr[low];
        arr[low] = arr[i];
        arr[i]= temp;
        return arr;
    }
    private int partition (int[] arr, int left, int right){
        int pivot = arr[right];
        int low = left-1;
        for (int i = left; i<right; i++){
            if (arr[i]<=pivot){
                low ++;
                arr = swap(arr, low, i);
            }
        }
        low = low+1;
        arr = swap(arr, low, right);
        return low;
    }

}
