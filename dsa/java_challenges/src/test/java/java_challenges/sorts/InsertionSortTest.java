package java_challenges.sorts;

import java_challenges.ArrayShift;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class InsertionSortTest {
    @Test
    public void testReturnSameArr() {
        InsertionSort classUnderTest = new InsertionSort();
        int[] arr = {1,2,3,4};
        assertEquals( arr, classUnderTest.insertionSort(arr));
    }
}
