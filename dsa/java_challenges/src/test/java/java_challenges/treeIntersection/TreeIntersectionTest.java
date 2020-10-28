package java_challenges.treeIntersection;

import data_structures.tree.NodeTree;
import data_structures.tree.Tree;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;

public class TreeIntersectionTest {
    private static Tree<Integer> makeTree(Tree<Integer> tree){
        tree.add(new NodeTree<>(500));
        tree.add(new NodeTree<>(10));
        tree.add(new NodeTree<>(30));
        tree.add(new NodeTree<>(50));
        tree.add(new NodeTree<>(1500));
        return tree;
    }
    @Test
    public void testTreeIntersectionOneNodeNoMatch(){
        Tree tree1 = new Tree(new NodeTree(5));
        Tree tree2 = new Tree(new NodeTree(10));
        ArrayList<Integer> expected = new ArrayList<>();
        Assert.assertEquals(expected, TreeIntersection.getTreeIntersection(tree1, tree2));

    }
    @Test
    public void testTreeIntersectionOneNodeOneMatch(){
        Tree tree1 = new Tree(new NodeTree(5));
        Tree tree2 = new Tree(new NodeTree(5));
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(5);
        Assert.assertEquals(expected, TreeIntersection.getTreeIntersection(tree1, tree2));

    }
    @Test
    public void testTreeIntersectionThrowsExceptionEmptyTree1(){
        Tree tree1 = new Tree();
        Tree tree2 = new Tree(new NodeTree(5));
        Assert.assertThrows("empty tree", Exception.class, ()-> TreeIntersection.getTreeIntersection(tree1, tree2));
    }
    @Test
    public void testTreeIntersectionThrowsExceptionEmptyTree2(){
        Tree tree1 = new Tree(new NodeTree(10));
        Tree tree2 = new Tree(new NodeTree());
        Assert.assertThrows("empty tree", Exception.class, ()-> TreeIntersection.getTreeIntersection(tree1, tree2));
    }
    @Test
    public void testTreeIntersectionManyNodesNoMatch(){
        Tree tree1 = makeTree(new Tree<Integer>());
        Tree tree2 = new Tree(new NodeTree(90));
        ArrayList<Integer> expected = new ArrayList<>();
        Assert.assertEquals(expected, TreeIntersection.getTreeIntersection(tree1, tree2));

    }
    @Test
    public void testTreeIntersectionManyNodesBothTreesNoMatch(){
        Tree tree1 = makeTree(new Tree<Integer>());
        Tree tree2 = new Tree(new NodeTree(90));
        tree2.add(new NodeTree(240));
        tree2.add(new NodeTree(2400));
        tree2.add(new NodeTree(20));
        tree2.add(new NodeTree(620));
        ArrayList<Integer> expected = new ArrayList<>();
        Assert.assertEquals(expected, TreeIntersection.getTreeIntersection(tree1, tree2));

    }
    @Test
    public void testTreeIntersectionManyNodesOneNodeOneMatch(){
        Tree tree1 = makeTree(new Tree<Integer>());
        Tree tree2 = new Tree(new NodeTree(1500));
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(1500);
        Assert.assertEquals(expected, TreeIntersection.getTreeIntersection(tree1, tree2));

    }
    @Test
    public void testTreeIntersectionManyNodesBothTreesMatch(){
        Tree tree1 = makeTree(new Tree<Integer>());
        Tree tree2 = new Tree(new NodeTree(90));
        tree2.add(new NodeTree(240));
        tree2.add(new NodeTree(2400));
        tree2.add(new NodeTree(20));
        tree2.add(new NodeTree(620));
        tree2.add(new NodeTree<>(10));
        tree2.add(new NodeTree<>(30));
        tree2.add(new NodeTree<>(50));
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(50);
        expected.add(10);
        expected.add(30);
        Assert.assertEquals(expected, TreeIntersection.getTreeIntersection(tree1, tree2));

    }
}
