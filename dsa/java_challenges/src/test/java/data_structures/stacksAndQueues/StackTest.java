package data_structures.stacksAndQueues;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

public class StackTest {
    @Test
    public void testEmptyStack(){
        Stack newStack = new Stack();
        assertNull(newStack.getTop());
    }
    @Test public void testPushOneValueInStack() throws Exception {
        Stack newStack = new Stack();
        newStack.push(5);
        assertEquals(5, newStack.peek());
        assertEquals("{5}=> NULL", newStack.toString());
    }
    @Test public void testPushMultipleValuesInStack() throws Exception {
        Stack newStack = new Stack();
        int[] values = {1,2,3,4,5};
        newStack.push(values);
        assertEquals(5, newStack.peek());
    }
    @Test public void testToStringForBigStack() throws Exception {
        Stack newStack = new Stack();
        int[] values = {1,2,3,4,5};
        newStack.push(values);
        assertEquals("{5}=> {4}=> {3}=> {2}=> {1}=> NULL", newStack.toString());
        assertEquals(5, newStack.peek());

    }
}
