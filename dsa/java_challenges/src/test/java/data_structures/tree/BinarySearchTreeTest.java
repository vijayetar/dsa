package data_structures.tree;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

public class BinarySearchTreeTest {
    // test instantiation
    @Test
    public void testEmptyTree(){
        BinarySearchTree tree = new BinarySearchTree();
        assertNull("empty tree", tree.root);
    }
    @Test public void testOneRootInTree(){
        NodeTree<Integer> nodeTree = new NodeTree<>(500);
        BinarySearchTree tree = new BinarySearchTree(nodeTree);
        assertEquals("Tree{root={value=500, left=null, right=null}}", tree.toString());
    }
    @Test public void testThreeNodesInTree(){
        BinarySearchTree tree = new BinarySearchTree(new NodeTree <Integer> (500));
        tree.add(new NodeTree<>(24));
        tree.add(new NodeTree<>(2400));
        assertEquals("Tree{root={value=500, left={value=24, left=null, right=null}, right={value=2400, left=null, right=null}}}", tree.toString());
    }
    @Test public void testSixNodesInTree(){
        BinarySearchTree tree = new BinarySearchTree(new NodeTree <Integer> (500));
        tree.add(new NodeTree<>(2400));
        tree.add(new NodeTree<>(24));
        tree.add(new NodeTree<>(12));
        tree.add(new NodeTree<>(400));
        assertEquals("Tree{root={value=500, left={value=24, left={value=12, left=null, right=null}, right={value=400, left=null, right=null}}, right={value=2400, left=null, right=null}}}", tree.toString());
    }
}
//    @Test public void testOneRootInTree(){
//        NodeTree<Integer> nodeTree = new NodeTree<>(500);
//        Tree tree = new Tree(nodeTree);
//        assertEquals("Tree{root={value=500, left=null, right=null}}", tree.toString());
//    }
//    @Test public void testThreeNodesInTree(){
//        NodeTree<Integer> left = new NodeTree<>(24);
//        NodeTree<Integer> right = new NodeTree<>(2400);
//        Tree tree = new Tree(new NodeTree <Integer> (500, left, right));
//        assertEquals("Tree{root={value=500, left={value=24, left=null, right=null}, right={value=2400, left=null, right=null}}}", tree.toString());
//    }
//}
