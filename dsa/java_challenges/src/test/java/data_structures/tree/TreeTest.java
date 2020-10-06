package data_structures.tree;

import org.junit.Test;

import java.util.ArrayList;
import java.util.EmptyStackException;

import static org.junit.Assert.*;

public class TreeTest {
    // create a helper function to isntantiate a new tree each time
    public Tree createTreeWithSixNodes(){
        Tree tree = new Tree();
        tree.add(new NodeTree<Integer>(500));
        tree.add(new NodeTree<Integer>(300));
        tree.add(new NodeTree<Integer>(5000));
        tree.add(new NodeTree<Integer>(10));
        tree.add(new NodeTree<Integer>(400));
        return tree;
    }
    // test instantiation
    @Test
    public void testEmptyTree(){
        Tree tree = new Tree();
        assertNull("empty tree", tree.root);
    }
    @Test public void testOneRootInTree(){
        NodeTree<Integer> nodeTree = new NodeTree<>(500);
        Tree tree = new Tree(nodeTree);
        assertEquals("Tree{root={value=500, left=null, right=null}}", tree.toString());
    }
    @Test public void testThreeNodesInTree(){
        NodeTree<Integer> left = new NodeTree<>(24);
        NodeTree<Integer> right = new NodeTree<>(2400);
        Tree tree = new Tree(new NodeTree <Integer> (500, left, right));
        assertEquals("Tree{root={value=500, left={value=24, left=null, right=null}, right={value=2400, left=null, right=null}}}", tree.toString());
    }
    // test add as a breadth first traversal
    @Test public void testAddOneNodeInTree(){
        Tree tree = new Tree();
        NodeTree<Integer> node = new NodeTree<>(5000);
        tree.add(node);
        System.out.println(tree.toString());
        NodeTree<Integer> nnode = new NodeTree<>(1000);
        tree.add(nnode);
        System.out.println(tree.toString());
        assertEquals("Tree{root={value=5000, left={value=1000, left=null, right=null}, right=null}}", tree.toString());
    }
    @Test public void testAddThreeNodesInTree(){
        Tree tree = new Tree();
        NodeTree<Integer> node = new NodeTree<>(5000);
        tree.add(node);
        NodeTree<Integer> nnode = new NodeTree<>(1000);
        tree.add(nnode);
        tree.add(new NodeTree<>(15000));
        assertEquals("Tree{root={value=5000, left={value=1000, left=null, right=null}, right={value=15000, left=null, right=null}}}", tree.toString());
    }
    @Test public void testAddFiveNodesInTree(){
        Tree tree = new Tree();
        tree.add(new NodeTree<Integer>(5000));
        tree.add(new NodeTree<Integer>(1000));
        tree.add(new NodeTree<Integer>(15000));
        tree.add(new NodeTree<Integer>(10));
        tree.add(new NodeTree<Integer>(15));
        assertEquals("Tree{root={value=5000, left={value=1000, left={value=10, left=null, right=null}, right={value=15, left=null, right=null}}, right={value=15000, left=null, right=null}}}", tree.toString());
    }
    // testing for preOrder method
    @Test public void testPreOrder(){
        Tree tree = createTreeWithSixNodes();
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(500);
        expected.add(300);
        expected.add(10);
        expected.add(400);
        expected.add(5000);
        assertEquals(expected, tree.preOrder());
    }
    // testing for preOrder method
    @Test public void testInOrder(){
        Tree tree = createTreeWithSixNodes();
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(10);
        expected.add(300);
        expected.add(400);
        expected.add(500);
        expected.add(5000);
        assertEquals(expected, tree.inOrder());
    }
    @Test public void testEmptyTreeOrder() throws EmptyStackException {
        Tree tree = new Tree();
        ArrayList<Integer> expected = new ArrayList<>();
        assertThrows("empty tree", Exception.class, ()-> tree.inOrder());
    }
    // testing for postOrder method
    @Test public void testPostOrder(){
        Tree tree = createTreeWithSixNodes();
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(10);
        expected.add(400);
        expected.add(300);
        expected.add(5000);
        expected.add(500);
        assertEquals(expected, tree.postOrder());
    }
    @Test public void testBreadthTraversalException() throws EmptyStackException{
        Tree tree = new Tree();
        assertThrows("empty tree", Exception.class, ()->tree.breadthTraversal());
    }
    @Test public void testBreadthTraversalOneNode() throws EmptyStackException{
        Tree tree = new Tree(new NodeTree<Integer>(500));
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(500);
        assertEquals(expected,tree.breadthTraversal());
    }
    @Test public void testBreadthTraversalMultipleNode() throws EmptyStackException{
        Tree tree = createTreeWithSixNodes();
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(500);
        expected.add(300);
        expected.add(5000);
        expected.add(10);
        expected.add(400);
        assertEquals(expected,tree.breadthTraversal());
    }
    
}
