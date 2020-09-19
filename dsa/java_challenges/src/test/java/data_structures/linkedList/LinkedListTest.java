package data_structures.linkedList;

import org.junit.Test;

import static junit.framework.TestCase.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class LinkedListTest {
    @Test
    public void testLinkedListEmpty(){
        LinkedList linkedList = new LinkedList();
        assertEquals("NULL", linkedList.toString());
    }
    @Test public void testLLsingleNode(){
        LinkedList linkedList = new LinkedList();
        linkedList.insert(4);
        assertEquals("{4} => NULL", linkedList.toString());
    }
    @Test public void testLLTwoNode(){
        LinkedList linkedList = new LinkedList();
        linkedList.insert(4);
        linkedList.insert(5);
        linkedList.insert(6);
        assertEquals("{6} => {5} => {4} => NULL", linkedList.toString());
    }
    @Test public void testisEmptyEmptyLL() {
        LinkedList linkedList = new LinkedList();
        assertTrue(linkedList.isEmpty());
    }
    @Test public void testisEmptyFullLL() {
        LinkedList linkedList = new LinkedList();
        linkedList.insert(4);
        assertFalse(linkedList.isEmpty());
    }
    @Test public void testLLIncludesTrue() {
        LinkedList linkedList = new LinkedList();
        linkedList.insert(4);
        linkedList.insert(5);
        linkedList.insert(6);
        assertTrue(linkedList.includes(6));
    }
    @Test public void testLLIncludesFalse() {
        LinkedList linkedList = new LinkedList();
        linkedList.insert(4);
        linkedList.insert(5);
        linkedList.insert(6);
        assertFalse(linkedList.includes(8));
    }
}
