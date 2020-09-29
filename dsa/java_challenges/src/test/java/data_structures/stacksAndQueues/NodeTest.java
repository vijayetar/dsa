package data_structures.stacksAndQueues;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

public class NodeTest {
    // test instantiation
    @Test
    public void testNodeEmptyInstantiation(){
        Node newNode = new Node();
        assertNull(newNode.getValue());
    }
    @Test public void testNodeToString(){
        Node newNode = new Node(5);
        assertEquals("{5}", newNode.toString());
    }
    @Test public void testNodeInstantiationToANode(){
        Node newNode = new Node(5);
        Node anotherNode = new Node(100, newNode);
        assertEquals("{100}", anotherNode.toString());
    }

}
