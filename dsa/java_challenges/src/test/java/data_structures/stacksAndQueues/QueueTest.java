package data_structures.stacksAndQueues;

import org.junit.Test;

import java.util.ArrayList;
import java.util.EmptyStackException;

import static org.junit.Assert.*;

public class QueueTest {
    @Test
    public void testEmptyQueue(){
        Queue<String> newQueue = new Queue();
        assertNull(newQueue.getFront());
    }
    @Test public void testEnqueueOneValueInQueue() throws EmptyStackException {
        Queue<Integer> newQueue = new Queue<>();
        newQueue.enqueue(5);
        assertEquals(5, (int) newQueue.peek());
        assertEquals("{5} => NULL", newQueue.toString());
    }
    @Test public void testEnqueueMultipleValuesInQueue() throws Exception {
        Queue<Integer> newQueue = new Queue<>();
        ArrayList<Integer> values = new ArrayList<>();
        values.add(1);
        values.add(3);
        values.add(7);
        newQueue.enqueue(values);
        assertFalse("check if empty", newQueue.isEmpty());
        assertEquals("{1} => {3} => {7} => NULL", newQueue.toString());
        assertEquals(1, (int) newQueue.peek());
    }
    @Test public void testPeekRaisesException() throws Exception {
        Queue<Integer> newQueue = new Queue<>();
        assertThrows("this is an empty queueu", Exception.class, ()-> newQueue.peek());
    }
    @Test public void testIsEmptyTrue(){
        Queue<Integer> newQueue = new Queue<>();
        assertTrue("the new stack is empty", newQueue.isEmpty());
    }
    @Test public void testIsEmptyFalse(){
        Queue<Integer> newQueue = new Queue<>();
        newQueue.enqueue(1);
        assertFalse("this stack is not empty", newQueue.isEmpty());
    }
    @Test public void testEmptyDequeueRaiseException() throws EmptyStackException {
        Queue<Integer> newQueue = new Queue<>();
        assertThrows("this is empty queue", Exception.class, ()-> newQueue.dequeue());
    }
    @Test public void testDequeue() throws EmptyStackException{
        Queue<Integer> newQueue = new Queue<>();
        ArrayList<Integer> values = new ArrayList<>();
        values.add(1);
        values.add(3);
        values.add(7);
        newQueue.enqueue(values);
        assertEquals(1, (int)newQueue.dequeue());
    }
    @Test public void testMultipleDequeueToEmpty() throws EmptyStackException {
        Queue<Integer> newQueue = new Queue<>();
        ArrayList<Integer> values = new ArrayList<>();
        values.add(1);
        values.add(3);
        values.add(7);
        newQueue.enqueue(values);
        newQueue.dequeue();
        newQueue.dequeue();
        newQueue.dequeue();
        assertThrows("this is empty stack", Exception.class, () -> newQueue.dequeue());
        assertTrue("the stack is empty", newQueue.isEmpty());
    }

}
