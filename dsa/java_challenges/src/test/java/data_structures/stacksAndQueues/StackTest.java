package data_structures.stacksAndQueues;

import org.junit.Test;

import java.util.ArrayList;
import java.util.EmptyStackException;

import static org.junit.Assert.*;

public class StackTest {
    @Test
    public void testEmptyStack(){
        Stack<Integer> newStack = new Stack();
        assertNull(newStack.getTop());
    }
    @Test public void testPushOneValueInStack() throws EmptyStackException {
        Stack<Integer> newStack = new Stack<>();
        newStack.push(5);
        assertEquals(5, (int) newStack.peek());
        assertEquals("{5}=> NULL", newStack.toString());
    }
    @Test public void testPushMultipleValuesInStack() throws Exception {
        Stack newStack = new Stack();
        ArrayList<Integer> values = new ArrayList<>();
        values.add(1);
        values.add(3);
        values.add(7);
        newStack.push(values);
        assertFalse("check if empty", newStack.isEmpty());
        assertEquals("{7}=> {3}=> {1}=> NULL", newStack.toString());
        assertEquals(7, (int) newStack.peek());
    }
    @Test public void testPeekRaisesException() throws Exception {
        Stack<String> newStack = new Stack<>();
        assertThrows("this is an empty stack", Exception.class, ()-> newStack.peek());
    }
    @Test public void testToStringForBigStack() throws Exception {
        Stack newStack = new Stack();
        ArrayList<Integer> values = new ArrayList<>();
        values.add(1);
        values.add(3);
        values.add(7);
        newStack.push(values);
        assertEquals("{7}=> {3}=> {1}=> NULL", newStack.toString());
        assertEquals(7, (int)newStack.peek());
    }
    @Test public void testIsEmptyTrue(){
        Stack newStack = new Stack();
        assertTrue("the new stack is empty", newStack.isEmpty());
    }
    @Test public void testIsEmptyFalse(){
        Stack newStack = new Stack();
        newStack.push(1);
        assertFalse("this stack is not empty", newStack.isEmpty());
    }
    @Test public void testPop() throws EmptyStackException{
        Stack newStack = new Stack();
        ArrayList<Integer> values = new ArrayList<>();
        values.add(1);
        values.add(3);
        values.add(7);
        newStack.push(values);
        assertEquals(7, newStack.pop());
    }
    @Test public void testEmptyPopRaiseException() throws EmptyStackException {
        Stack newStack = new Stack();
        assertThrows("this is empty stack", Exception.class, ()-> newStack.pop());
    }
    @Test public void testMultiplePopsToEmpty() throws EmptyStackException {
        Stack newStack = new Stack();
        ArrayList<Integer> values = new ArrayList<>();
        values.add(1);
        values.add(3);
        values.add(7);
        newStack.push(values);
        newStack.pop();
        newStack.pop();
        newStack.pop();
        assertThrows("this is empty stack", Exception.class, () -> newStack.pop());
        assertTrue("the stack is empty", newStack.isEmpty());g
    }
}
