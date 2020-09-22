package data_structures.linkedList;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import static junit.framework.TestCase.assertEquals;
import static org.junit.Assert.*;

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
    @Test public void testLLOneappend(){
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        assertEquals("{1} => NULL", linkedList.toString());

    }
    @Test public void testLLTwoappend(){
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        assertEquals("{1} => {2} => {3} => NULL", linkedList.toString());

    }
    @Test public void testInsertAfterPresentValue(){
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        assertEquals("{1} => {2} => {500} => {3} => NULL", linkedList.insertAfter(2, 500));

    }
    @Test public void testInsertAfterHeadValue(){
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(5);
        assertEquals("{1} => {5000} => {5} => NULL", linkedList.insertAfter(1, 5000));

    }
    @Test public void testInsertAfterAbsentValue(){
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        assertEquals("value not in linked list", linkedList.insertAfter(5, 500));

    }
    @Test public void testInsertBeforePresentValue(){
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        assertEquals("{1} => {500} => {2} => {3} => NULL", linkedList.insertBefore(2, 500));

    }
    @Test public void testInsertBeforeAbsentValue(){
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        assertEquals("value not in linked list", linkedList.insertBefore(6, 500));

    }
    @Test public void testInsertBeforeHeadValue(){
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        assertEquals("{500} => {1} => {2} => {3} => NULL", linkedList.insertBefore(1,500));
    }
    @Test public void testKthFromTheEnd () throws Exception{
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        linkedList.append(4);
        linkedList.append(5);
        linkedList.append(6);
        assertEquals(4, linkedList.kthFromEnd(2));
    }
    @Test public void testKthFromTheEndEqualsLength () throws Exception{
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        linkedList.append(4);
        linkedList.append(5);
        linkedList.append(6);
        assertEquals(1, linkedList.kthFromEnd(6));
    }
    @Test public void testKthFromTheEndNegativeInteger () throws Exception{
        LinkedList linkedList = new LinkedList();
        linkedList.append(1);
        linkedList.append(2);
        linkedList.append(3);
        linkedList.append(4);
        linkedList.append(5);
        linkedList.append(6);
        assertEquals(3, linkedList.kthFromEnd(-3));
    }
//    @Test public void testKthFromTheEndOneNode () throws Exception{
//        LinkedList linkedList = new LinkedList();
//        linkedList.append(1);
//        assertThrows("", linkedList.kthFromEnd(5));
//    }

}
