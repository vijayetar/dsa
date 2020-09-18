package DataStructures.LinkedList;
import org.junit.Assert;
import org.junit.Test;

import static junit.framework.TestCase.assertEquals;

public class LinkedListTest {
    @Test
    public void testLinkedListEmpty(){
        LinkedList linkedList = new LinkedList();
        assertEquals("NULL", linkedList.toString());
    }
    @Test public void testTestInt(){
        LinkedList testClass = new LinkedList();
        assertEquals(2, testClass.testInt());
    }
}
