public class ArrayReverse{
    public static void main(String[] args){
        System.out.println("In the array reverse function");
        int[] testArr1 = {
            1, 2, 3, 4, 5, 6
        };
        arrayReverse(testArr1);
        int[] testArr2 = {
            89, 2354, 3546, 23, 10, -923, 823, -12
        };
        arrayReverse(testArr2);
        int[] testArr3 = {
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
        };
        arrayReverse(testArr3);
    }
    public static void arrayReverse(int[] testArr){
        int temp;
        int l = testArr.length;
        int mid = l%2 ==0? l/2:l/2+1;
        for (int i = 0; i<mid;i++ ){
            temp = testArr[i];
            testArr[i]=testArr[l-1-i];
            testArr[l-1-i]=temp;
        }
        for (int i=0; i<testArr.length; i++){
            System.out.println(testArr[i]);
        }
    }
}
