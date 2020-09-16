package java_challenges;

public class BinarySearch {
    public boolean someLibraryMethod() {
        return true;
    }
    //function that takes in a sorted array, and a number and returns the index if the number present in the array or else, returns -1
    public int binarySearchArray(int[] inputArray, int num){
        //define variables
        int start = 0;
        int end = inputArray.length-1;
        int mid = (start+end)/2;
        //while loop to check through the array until only one number is left
        while (mid!=start && mid!=end){
            if (inputArray[mid]==num){
                return mid;
            }
            else {
                if(inputArray[mid]<num){
                    start = mid+1;

                } else {
                    end = mid-1;
                }
            }
            mid = (start+end)/2;
        }
        int returnNum = inputArray[mid]==num?mid:-1;
        return returnNum;
    }
}
