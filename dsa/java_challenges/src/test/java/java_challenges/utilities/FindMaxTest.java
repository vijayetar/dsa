package java_challenges.utilities;

import data_structures.tree.NodeTree;
import data_structures.tree.Tree;
import org.junit.Test;

import java.util.EmptyStackException;

import static org.junit.Assert.*;

public class FindMaxTest {
    @Test public void testFindMaxException(){
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>();
        assertThrows("this is empty tree", Exception.class, ()->findMax.findMaxNumber(newTree));
    }
    @Test public void testFindMaxRoot(){
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>();
        newTree.add(new NodeTree<Integer> (500));
        assertEquals(500,findMax.findMaxNumber(newTree));
    }
    @Test public void testFindMaxNode(){
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>();
        newTree.add(new NodeTree<Integer> (500));
        newTree.add(new NodeTree<Integer> (20));
        newTree.add(new NodeTree<Integer> (40));
        newTree.add(new NodeTree<Integer> (529));
        assertEquals(529,findMax.findMaxNumber(newTree));
    }
    @Test public void testFindMaxNodeNegativeNumbers(){
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>();
        newTree.add(new NodeTree<Integer> (-500));
        newTree.add(new NodeTree<Integer> (-20));
        newTree.add(new NodeTree<Integer> (-40));
        newTree.add(new NodeTree<Integer> (-529));
        assertEquals(-20,findMax.findMaxNumber(newTree));
    }
    @Test public void testFindMaxSumInstantiation() throws EmptyStackException {
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>();
        assertThrows("empty tree", Exception.class, ()->findMax.findMaxSum(newTree));
    }
    @Test public void testFindMaxSumOneRoot() throws EmptyStackException {
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>(new NodeTree<Integer> (20));
        assertEquals(20, findMax.findMaxSum(newTree));
    }
    @Test public void testFindMaxSumTwoNodes() throws EmptyStackException {
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>(new NodeTree<Integer> (20));
        newTree.add(new NodeTree<Integer>(400));
        assertEquals(420, findMax.findMaxSum(newTree));
    }
    @Test public void testFindMaxSumThreeNodes() throws EmptyStackException {
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>(new NodeTree<Integer> (20));
        newTree.add(new NodeTree<Integer>(400));
        newTree.add(new NodeTree<Integer>(600));
        assertEquals(620, findMax.findMaxSum(newTree));
    }
    @Test public void testFindMaxSumMultipleNodes() throws EmptyStackException {
        FindMax findMax = new FindMax();
        Tree<Integer> newTree = new Tree<>(new NodeTree<Integer> (20));
        newTree.add(new NodeTree<Integer>(-400));
        newTree.add(new NodeTree<Integer>(600));
        newTree.add(new NodeTree<Integer>(600));
        newTree.add(new NodeTree<Integer>(600));
        newTree.add(new NodeTree<Integer>(-600));
        newTree.add(new NodeTree<Integer>(-600));
        assertEquals(220, findMax.findMaxSum(newTree));
    }
}
