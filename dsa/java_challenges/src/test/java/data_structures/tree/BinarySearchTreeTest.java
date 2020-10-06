package data_structures.tree;

import org.junit.Test;

import static org.junit.Assert.*;

public class BinarySearchTreeTest {
    // test instantiation
    @Test
    public void testEmptyTree(){
        BinarySearchTree tree = new BinarySearchTree();
        assertNull("empty tree", tree.root);
    }
    @Test public void testOneRootInTree(){
        BinarySearchTree tree = new BinarySearchTree(500);
        assertEquals("BinarySearchTree{root={value=500, left=null, right=null}}", tree.toString());
    }
    @Test public void testFourNodesInTree(){
        BinarySearchTree tree = new BinarySearchTree();
        tree.add(500);
        tree.add(24);
        tree.add(2400);
        tree.add(1000);
        assertEquals("BinarySearchTree{root={value=500, left={value=24, left=null, right=null}, right={value=2400, left={value=1000, left=null, right=null}, right=null}}}", tree.toString());
    }
//    @Test public void testSixNodesInTree(){
//        BinarySearchTree tree = new BinarySearchTree(500);
//        tree.add(2400);
//        tree.add(24);
//        tree.add(12);
//        tree.add(400);
//        assertEquals("BinarySearchTree{root={value=500, left={value=24, left={value=12, left=null, right=null}, right={value=400, left=null, right=null}}, right={value=2400, left=null, right=null}}}", tree.toString());
//    }
//    @Test public void testContainsThrowsException(){
//        BinarySearchTree tree = new BinarySearchTree();
//        assertThrows("empty tree", Exception.class, ()->tree.contains(500));
//    }
//    @Test public void testContainsRootTrue(){
//        BinarySearchTree tree = new BinarySearchTree(500);
//        assertTrue("contains 500", tree.contains(500));
//    }
//    @Test public void testContainsFalse(){
//        BinarySearchTree tree = new BinarySearchTree(500);
//        assertFalse("doesnot contain root value", tree.contains(1000));
//    }
//    @Test public void testContainsOneEdgeTrue(){
//        BinarySearchTree tree = new BinarySearchTree(500);
//        tree.add(100);
//        tree.add(55);
//        tree.add(650);
//        System.out.println(tree.toString());
//        assertTrue("does contain value", tree.contains(650));
//    }
//    @Test public void testContainsThreeEdgesTrue(){
//        BinarySearchTree tree = new BinarySearchTree(500);
//        tree.add(100);
//        tree.add(55);
//        tree.add(25);
//        tree.add(650);
//        tree.add(899);
//        tree.add(1000);
//        System.out.println(tree.toString());
//        assertTrue("does contain value", tree.contains(1000));
//    }
//    @Test public void testContainsThreeEdgesFalse(){
//        BinarySearchTree tree = new BinarySearchTree(500);
//        tree.add(100);
//        tree.add(55);
//        tree.add(25);
//        tree.add(650);
//        tree.add(899);
//        tree.add(1000);
//        System.out.println(tree.toString());
//        assertFalse("does not contain value", tree.contains(1001));
//    }
}

