package java_challenges.sorts;

import org.junit.Assert;
import org.junit.Test;

public class QuickSortTest {
    @Test
    public void testReturnSameArrOneNum() {
        QuickSort classUnderTest = new QuickSort();
        int[] arr = {1};
        int[] expected = {1};
        Assert.assertArrayEquals(expected, classUnderTest.quickSort(arr));
    }
    @Test
    public void testReturnSameSortedArr() {
        QuickSort classUnderTest = new QuickSort();
        int[] arr = {1,2,3,4};
        int[] expected = {1,2,3,4};
        Assert.assertArrayEquals(expected, classUnderTest.quickSort(arr));
    }
    @Test
    public void testReturnSortedArrShort() {
        QuickSort classUnderTest = new QuickSort();
        int[] arr = {4,3};
        int[] expected = {3,4};
        Assert.assertArrayEquals(expected, classUnderTest.quickSort(arr));
    }
    @Test
    public void testReturnSortedArrLong() {
        QuickSort classUnderTest = new QuickSort();
        int[] arr = {4,3,2};
        int[] expected = {2,3,4};
        classUnderTest.quickSort(arr);
        Assert.assertArrayEquals(expected, classUnderTest.quickSort(arr));

    }
    @Test
    public void testReturnSortedArrNegInt() {
        QuickSort classUnderTest = new QuickSort();
        int[] arr = {-4,3,-2,200,-500,100,-850};
        int[] expected = {-850,-500,-4,-2,3,100,200};
        Assert.assertArrayEquals(expected, classUnderTest.quickSort(arr));
    }
}
