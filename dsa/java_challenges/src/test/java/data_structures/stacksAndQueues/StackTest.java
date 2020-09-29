package data_structures.stacksAndQueues;

import org.junit.Test;

import static org.junit.Assert.*;

public class StackTest {
    @Test
    public void testEmptyStack(){
        Stack<T> newStack = new Stack();
        assertNull(newStack.getTop());
    }
//    @Test public void testPushOneValueInStack() throws Exception {
//        Stack<T> newStack = new Stack<T>();
//        newStack.push(5);
//        assertEquals(5, newStack.peek());
//        assertEquals("{5}=> NULL", newStack.toString());
//    }
//    @Test public void testPushMultipleValuesInStack() throws Exception {
//        Stack newStack = new Stack();
//        int[] values = new int[]{1,2,3,4,5};
//        newStack.push(values);
//        assertEquals(5, (int)newStack.peek());
//    }
//    @Test public void testPeekRaisesException() throws Exception {
//        Stack<T> newStack = new Stack<T>();
//        assertThrows("this is an empty stack", Exception.class, ()-> newStack.peek());
//    }
//    @Test public void testToStringForBigStack() throws Exception {
//        Stack newStack = new Stack();
//        int[] values = {1,2,3,4,5};
//        newStack.push(values);
//        assertEquals("{5}=> {4}=> {3}=> {2}=> {1}=> NULL", newStack.toString());
//        assertEquals(5, newStack.peek());
//    }
//    @Test public void testIsEmptyTrue(){
//        Stack newStack = new Stack();
//        assertTrue("the new stack is empty", newStack.isEmpty());
//    }
//    @Test public void testIsEmptyFalse(){
//        Stack newStack = new Stack();
//        newStack.push(1);
//        assertFalse("this stack is not empty", newStack.isEmpty());
//    }
//    @Test public void testEmptyPopRaiseException(){
//        Stack newStack = new Stack();
//
//    }

}
