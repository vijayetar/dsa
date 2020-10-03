package java_challenges.utilities;

import data_structures.stacksAndQueues.Queue;
import org.junit.Test;

import java.util.Collection;
import java.util.EmptyStackException;
import java.util.Iterator;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

public class DuckDuckGooseTest {
    @Test
    public void testEmptyQueue() throws EmptyStackException {
        Queue<String> q = new Queue<>();
        DuckDuckGoose ddg = new DuckDuckGoose();
        assertThrows("empty Queue", Exception.class, ()->ddg.ddG(q, 5) );
    }
    @Test public void testInvalidInteger() throws IllegalArgumentException{
        Queue<String> q = new Queue<>();
        q.enqueue("First");
        DuckDuckGoose ddg = new DuckDuckGoose();
        assertThrows("illegal integer below 0", Exception.class, ()->ddg.ddG(q, -9) );

    }
    @Test public void testSingleQueueElement() throws IllegalArgumentException{
        Queue<String> q = new Queue<>();
        q.enqueue("First");
        DuckDuckGoose ddg = new DuckDuckGoose();
        assertEquals("First", ddg.ddG(q, 5));
    }
    @Test public void testMultipleQueueElement() throws IllegalArgumentException{
        Queue<String> q = new Queue<>();
        q.enqueue("First");
        q.enqueue("Second");
        q.enqueue("Third");
        DuckDuckGoose ddg = new DuckDuckGoose();
        assertEquals("Third", ddg.ddG(q, 1));
    }
    @Test public void testFiveQueueElement() throws IllegalArgumentException{
        Queue<String> q = new Queue<>();
        q.enqueue("First");
        q.enqueue("Second");
        q.enqueue("Third");
        q.enqueue("Fourth");
        q.enqueue("Fifth");
        DuckDuckGoose ddg = new DuckDuckGoose();
        assertEquals("Fourth", ddg.ddG(q, 3));
    }
}
