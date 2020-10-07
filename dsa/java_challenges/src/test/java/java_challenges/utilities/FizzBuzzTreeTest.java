package java_challenges.utilities;

import data_structures.tree.NodeTree;
import data_structures.tree.Tree;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

public class FizzBuzzTreeTest {
    @Test
    public void testEmptyTreeException(){
        Tree<Integer> tree = new Tree<>();
        FizzBuzzTree fbTree = new FizzBuzzTree();
        assertThrows("empty tree given", Exception.class, ()-> fbTree.makeNewFBtree(tree));

    }
    @Test
    public void testOneNodeInGivenTree(){
        Tree<Integer> tree = new Tree<>(new NodeTree<Integer>(1500));
        FizzBuzzTree fbTree = new FizzBuzzTree();
        assertEquals("Tree{root={value=FizzBuzz, left=null, right=null}}", fbTree.makeNewFBtree(tree).toString());

    }
    @Test public void testThreeNodesInGivenTree(){
        Tree<Integer> tree = new Tree<>(new NodeTree<Integer>(1500));
        tree.add(new NodeTree<Integer> (500));
        tree.add(new NodeTree<Integer>(300));
        FizzBuzzTree fbTree = new FizzBuzzTree();
        assertEquals("Tree{root={value=FizzBuzz, left={value=Buzz, left=null, right=null}, right={value=FizzBuzz, left=null, right=null}}}", fbTree.makeNewFBtree(tree).toString());
    }
    @Test public void testFourNodesInGivenTree(){
        Tree<Integer> tree = new Tree<>(new NodeTree<Integer>(1500));
        tree.add(new NodeTree<Integer> (500));
        tree.add(new NodeTree<Integer>(300));
        tree.add(new NodeTree<Integer>(2));
        tree.add(new NodeTree<Integer>(330));
        System.out.println(tree.toString());
        FizzBuzzTree fbTree = new FizzBuzzTree();
        assertEquals("Tree{root={value=FizzBuzz, left={value=Buzz, left={value=2, left=null, right=null}, right={value=FizzBuzz, left=null, right=null}}, right={value=FizzBuzz, left=null, right=null}}}", fbTree.makeNewFBtree(tree).toString());
    }
}
