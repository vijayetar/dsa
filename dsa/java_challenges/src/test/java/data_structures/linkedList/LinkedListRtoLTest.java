//package data_structures.linkedList;
//
//import org.junit.Test;
//
//import static junit.framework.TestCase.assertEquals;
//import static org.junit.Assert.*;
//
//public class LinkedListRtoLTest {
//    @Test
//    public void testLinkedListEmpty(){
//        LinkedListRtoL linkedListRtoL = new LinkedListRtoL();
//        assertEquals("NULL", linkedListRtoL.toString());
//    }
//    @Test public void testLLsingleNode(){
//        LinkedListRtoL linkedListRtoL = new LinkedListRtoL();
//        linkedListRtoL.addToFront(4);
//        assertEquals("{4} => NULL", linkedListRtoL.toString());
//    }
//    @Test public void testLLshowHead(){
//        LinkedListRtoL linkedListRtoL = new LinkedListRtoL();
//        linkedListRtoL.addToFront(4);
//        assertEquals("This is the head of the Linked List: : 4", linkedListRtoL.showHead());
//    }
//    @Test public void testLLIncludesTrue() {
//        LinkedListRtoL linkedListRtoL = new LinkedListRtoL();
//        linkedListRtoL.addToFront(4);
//        linkedListRtoL.addToFront(5);
//        linkedListRtoL.addToFront(6);
//        assertTrue(linkedListRtoL.includes(6));
//    }
//    @Test public void testLLIncludesFalse() {
//        LinkedListRtoL linkedListRtoL = new LinkedListRtoL();
//        linkedListRtoL.addToFront(4);
//        linkedListRtoL.addToFront(5);
//        linkedListRtoL.addToFront(6);
//        assertFalse(linkedListRtoL.includes(8));
//    }
//    @Test public void testKthFromTheEnd () throws Exception{
//        LinkedListRtoL linkedListRtoL = new LinkedListRtoL();
//        linkedListRtoL.addToFront(4);
//        linkedListRtoL.addToFront(5);
//        linkedListRtoL.addToFront(6);
//        assertEquals(5, linkedListRtoL.kthFromEnd(1));
//    }
//    @Test public void testKthFromTheEndException() throws Exception{
//        LinkedListRtoL linkedListRtoL = new LinkedListRtoL();
//        linkedListRtoL.addToFront(4);
//        linkedListRtoL.addToFront(5);
//        linkedListRtoL.addToFront(6);
//        assertThrows("It looks like the linked list is too short!", Exception.class, ()->linkedListRtoL.kthFromEnd(4));
//    }
//
//}
