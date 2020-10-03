package data_structures.tree;

import org.junit.Test;

import static org.junit.Assert.*;

public class NodeTreeTest {
    // test instantiation
    @Test
    public void testNodeTreeEmpty(){
        NodeTree<Integer> node = new NodeTree<>();
        assertEquals("{value=null, left=null, right=null}", node.toString());
    }
    @Test
    public void testNodeTreeValue(){
        NodeTree<Integer> node = new NodeTree<>(300);
        assertEquals("{value=300, left=null, right=null}", node.toString());
    }
    @Test public void testNodeTreeValueLeftRight(){
        NodeTree<Integer> leftNode = new NodeTree<>(200);
        NodeTree<Integer> rightNode = new NodeTree<>(700);
        NodeTree<Integer> node = new NodeTree<>(300, leftNode, rightNode);
        assertEquals("{value=300, left={value=200, left=null, right=null}, right={value=700, left=null, right=null}}", node.toString());
    }
    // test methods
    @Test public void testNodeIsNullTrue(){
        NodeTree<Integer> node = new NodeTree<>();
        assertTrue("the value is null", node.isNull());
    }
    @Test public void testNodeIsNullFalse(){
        NodeTree<Integer> node = new NodeTree<>();
        node.value = 5;
        assertFalse("the value is not null", node.isNull());
    }
}
