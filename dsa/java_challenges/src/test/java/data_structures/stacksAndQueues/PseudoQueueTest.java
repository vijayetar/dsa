package data_structures.stacksAndQueues;

import org.junit.Test;

import java.util.EmptyStackException;

import static org.junit.Assert.*;

public class PseudoQueueTest {
    // test enqueue and dequeue
    @Test
    public void testNewPsuedoQueue(){
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        assertTrue("empty pseduqueue", newQueue.isEmpty());
    }
    @Test public void testEnqueue(){
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        newQueue.enqueue(5);
        assertFalse("it is not empty", newQueue.isEmpty());
    }
    @Test public void testPeekFull(){
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        newQueue.enqueue(5);
        assertEquals(5, (int)newQueue.peek());
    }
    @Test public void testPeekEmpty () throws EmptyStackException {
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        assertThrows("empty queue", Exception.class, ()->newQueue.peek());
    }
    @Test public void testDequeueFull(){
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        newQueue.enqueue(5);
        assertEquals(5, (int) newQueue.dequeue());
    }
    @Test public void testEnqueMultiple(){
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        newQueue.enqueue(5);
        newQueue.enqueue(10);
        newQueue.enqueue(15);
        newQueue.enqueue(25);
        assertEquals(5, (int)newQueue.peek());
    }
    @Test public void testDequeMultiple(){
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        newQueue.enqueue(5);
        newQueue.enqueue(10);
        newQueue.enqueue(15);
        newQueue.enqueue(25);
        assertEquals(5, (int)newQueue.dequeue());
    }
    @Test public void testDequeMultipleTillEmpty(){
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        newQueue.enqueue(5);
        newQueue.enqueue(10);
        newQueue.enqueue(15);
        newQueue.enqueue(25);
        newQueue.dequeue();
        newQueue.dequeue();
        newQueue.dequeue();
        newQueue.dequeue();
        assertTrue("empty pseduqueue", newQueue.isEmpty());
    }
    @Test public void testToString(){
        PseudoQueue<Integer> newQueue = new PseudoQueue<>();
        newQueue.enqueue(5);
        newQueue.enqueue(10);
        newQueue.enqueue(15);
        newQueue.enqueue(25);
        assertEquals("", newQueue.toString());
    }

}
