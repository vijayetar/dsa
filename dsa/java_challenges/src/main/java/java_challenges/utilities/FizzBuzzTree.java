package java_challenges.utilities;

import data_structures.tree.NodeTree;
import data_structures.tree.Tree;

import java.util.EmptyStackException;

public class FizzBuzzTree extends Tree<String> {
    // method that takes in a tree
    // returns a new tree with fizz buzz or string
    public Tree<String> makeNewFBtree(Tree<Integer> tree) throws EmptyStackException{
        Tree<String> newTree = new Tree<>();
        if (tree.isEmpty()){
            throw new EmptyStackException();
        }
        // create a tree with a breadth traversal
        newTree.root = walk(tree.root);
        return newTree;
    }
    // recursive function walk to traverse the original tree in depth first manner and then create a new node with the fizzbuzzed value of the node
    private NodeTree<String> walk (NodeTree<Integer> rootNode){
        if (rootNode == null){
            return null;
        }
        NodeTree<String> newRootNode = createFizzBuzz(rootNode);
        newRootNode.left = walk(rootNode.left);
        newRootNode.right = walk(rootNode.right);
        return newRootNode;
    }

    // helper function that takes in a Node and returns a new Node of string "Fizz" "Buzz" "FizzBuzz" or "value of initial Node as string"
    private NodeTree<String> createFizzBuzz(NodeTree<Integer> intNode){
        if (intNode.value%5==0 && intNode.value%3==0){
            return new NodeTree<String>("FizzBuzz");
        }
        else if (intNode.value %5==0){
            return new NodeTree<String>("Buzz");
        }
        else if (intNode.value%3 ==0){
            return new NodeTree<String>("Fizz");
        }
        return new NodeTree<String>(String.valueOf(intNode.value)); //https://www.javatpoint.com/java-int-to-string
    }
}
