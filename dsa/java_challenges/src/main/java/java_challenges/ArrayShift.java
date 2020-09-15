package java_challenges;

public class ArrayShift {
    public boolean someLibraryMethod() {
        return true;
    }
    public int[] insertShiftArray(int[] inputArray, int val){
        int arrayLength = inputArray.length;
        int mid = arrayLength%2 == 0 ? arrayLength/2:arrayLength/2+1;
        int[] newArray = new int[arrayLength+1];
        System.out.println(arrayLength + "and" + mid);
        if (mid==0){
            newArray[0]=val;
            return newArray;
        }
        for (int i = 0; i<arrayLength; i++){
            if (i == mid){
                newArray[mid]=val;
            } else if (i>mid){
                newArray[i]=inputArray[i-1];
            } else {
                newArray[i]=inputArray[i];
            }
        }
        newArray[arrayLength]= inputArray[arrayLength-1];
        return newArray;
    }
}
