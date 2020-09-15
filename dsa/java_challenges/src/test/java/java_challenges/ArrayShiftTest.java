package java_challenges;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class ArrayShiftTest {
    @Test
    public void testSomeLibraryMethod() {
        ArrayShift classUnderTest = new ArrayShift();
        assertTrue("someLibraryMethod should return 'true'", classUnderTest.someLibraryMethod());
    }
    @Test public void testInsertShiftArrayEvenArray(){
        ArrayShift arrayShift = new ArrayShift();
        int[] arrayInput = {2,2,2,2};
        int[] arrayExpected = {2,2,3,2,2};
        Assert.assertArrayEquals(arrayExpected, arrayShift.insertShiftArray(arrayInput, 3));
    }
    @Test public void testInsertShiftArrayEdgeOne(){
        ArrayShift arrayShift = new ArrayShift();
        int[] arrayInput = {};
        int[] arrayExpected = {3};
        Assert.assertArrayEquals(arrayExpected, arrayShift.insertShiftArray(arrayInput, 3));
    }
    @Test public void testInsertShiftArrayOddArray(){
        ArrayShift arrayShift = new ArrayShift();
        int[] arrayInput = {2,2,2};
        int[] arrayExpected = {2,2,3,2};
        Assert.assertArrayEquals(arrayExpected, arrayShift.insertShiftArray(arrayInput, 3));
    }
    @Test public void testInsertShiftArrayNegativeValue(){
        ArrayShift arrayShift = new ArrayShift();
        int[] arrayInput = {2,2,2};
        int[] arrayExpected = {2,2,-3,2};
        Assert.assertArrayEquals(arrayExpected, arrayShift.insertShiftArray(arrayInput, -3));
    }
}
