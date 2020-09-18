package java_challenges;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class BinarySearchTest {
    @Test
    public void testSomeLibraryMethod() {
        BinarySearch classUnderTest = new BinarySearch();
        assertTrue("someLibraryMethod should return 'true'", classUnderTest.someLibraryMethod());
    }
    @Test public void testBinarySearchArrayNegativeOne(){
        BinarySearch binarySearch = new BinarySearch();
        int[] inputArray = {11,22,33,44,55,66,77};
        int num = 90;
        assertEquals(-1, binarySearch.binarySearchArray(inputArray, num));
    }
    @Test public void testBinarySearchArrayPositiveOne(){
        BinarySearch binarySearch = new BinarySearch();
        int[] inputArray = {4,8,15,16,23,42};
        int num = 15;
        assertEquals(2, binarySearch.binarySearchArray(inputArray, num));
    }
    @Test public void testBinarySearchArraySingleArray(){
        BinarySearch binarySearch = new BinarySearch();
        int[] inputArray = {5};
        int num = 5;
        assertEquals(0, binarySearch.binarySearchArray(inputArray, num));
    }

}
