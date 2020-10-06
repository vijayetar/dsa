package java_challenges.utilities;

import data_structures.tree.NodeTree;
import data_structures.tree.Tree;

import java.util.Arrays;
import java.util.EmptyStackException;
import java.util.List;

public class FindMax extends Tree <Integer> {
    public int findMaxNumber(Tree<Integer> tree) throws EmptyStackException {
        if (tree.isEmpty()){
            throw new EmptyStackException();
        }
        int max = tree.root.value;
        return walk(tree.root, max);
    }
    private int walk(NodeTree<Integer> rootNode, int max){
        if (rootNode == null){
            return max;
        }
        if (max< rootNode.value){
            max = rootNode.value;
        }
        max = walk(rootNode.left, max);
        max = walk(rootNode.right, max);
        return max;
    }
    // this function find the maximum sum of the nodes of the tree to the leaf
    public int findMaxSum(Tree<Integer> tree) throws EmptyStackException {
        if (tree.isEmpty()){
            throw new EmptyStackException();
        }
        int maxSum = tree.root.value;
        int sum = 0;
        List<Object> theSums = Arrays.asList(maxSum, sum);
        theSums = getSum(tree.root, theSums);
        return (int) theSums.get(0);
    }
    private List<Object> getSum(NodeTree<Integer> rootNode, List<Object> theSums) {
        if (rootNode == null) {
            if ((int) theSums.get(1) > (int) theSums.get(0)) { //this is checking if the maxSum is greater than the sum
                theSums.set(0, theSums.get(1)); //this is setting the max Sum to the value of sum
            }
            return theSums; // returns maxSum and sum
        }
        int newSum = (int) theSums.get(1) + rootNode.value; // this is adding the sum to the value of the rootNode
        theSums.set(1, newSum); //sets the value of the sum to the new sum with the root node.

        theSums = getSum(rootNode.left, theSums);
        if (rootNode.left != null) {
            //subtract the sum of that value
            newSum = (int) theSums.get(1) - rootNode.left.value;
            theSums.set(1, newSum);
        }
        theSums = getSum(rootNode.right, theSums);
        if (rootNode.right != null) {
            //subtract the sum of that value
            newSum = (int) theSums.get(1) - rootNode.right.value;
            theSums.set(1, newSum);
        }
        return theSums;
    }


}
