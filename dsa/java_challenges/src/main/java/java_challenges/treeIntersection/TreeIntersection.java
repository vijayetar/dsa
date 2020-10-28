package java_challenges.treeIntersection;

import data_structures.tree.NodeTree;
import data_structures.tree.Tree;

import java.util.ArrayList;
import java.util.EmptyStackException;

public class TreeIntersection {

    public static ArrayList<Integer> getTreeIntersection(Tree<Integer> tree1, Tree<Integer> tree2) throws EmptyStackException{
        if (tree1.root == null | tree2.root == null){
            throw new EmptyStackException();
        }
        ArrayList<Integer> output = new ArrayList<>();
        ArrayList<Integer> tree1Nodes = new ArrayList<>();
        tree1Nodes = tree1.preOrder();
        // traverse the second tree and check for matching nodes
        NodeTree<Integer> current = tree1.root;
        output = traverseTree(tree2.root, tree1Nodes, output);
        return output;
    }
    private static ArrayList<Integer> traverseTree(NodeTree root, ArrayList<Integer> tree1Nodes, ArrayList<Integer> output){
        if (root == null){
            return output;
        }
        if (tree1Nodes.contains(root.value)){
            output.add((Integer) root.value);
        }
        output = traverseTree(root.left, tree1Nodes, output);
        output = traverseTree(root.right, tree1Nodes,  output);
        return output;
    }
}
