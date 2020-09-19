package data_structures.linkedList;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class NodeTest {
    @Test
    public void testNode(){
        Node node = new Node(5);
        assertEquals("{5}", node.toString());
    }
}
