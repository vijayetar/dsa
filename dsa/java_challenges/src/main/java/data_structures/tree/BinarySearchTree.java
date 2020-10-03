package data_structures.tree;

import java.util.EmptyStackException;

public class BinarySearchTree {
    NodeTree<Integer> root = null;

    public BinarySearchTree() {
        this.root = null;
    }

    public BinarySearchTree(Integer val) {
        this.root = new NodeTree<Integer>(val);
    }

    // add integer to the tree recursively using _walk method
    public void add(Integer val) {
        if (this.root == null) {
            this.root = new NodeTree<Integer>(val);
            return;
        }
        root = _walk(this.root, val);
    }

    private NodeTree<Integer> _walk(NodeTree<Integer> current, Integer val) {
        if (val > current.value) {
            if (current.right == null) {
                current.right = new NodeTree<Integer>(val);
                return current;
            }
            current.right = _walk(current.right, val);
        } else if (val < current.value) {
            if (current.left == null) {
                current.left = new NodeTree<Integer>(val);
                return current;
            }
            current.left = _walk(current.left, val);
        }
        return current;
    }

    public boolean contains(Integer val) throws EmptyStackException {
        if (root == null) {
            throw new EmptyStackException();
        }
        return _walkCheck(root, val);
    }

    private boolean _walkCheck(NodeTree<Integer> rootNode, Integer val) {
        System.out.println(rootNode.value + " value: "+val);
        if (rootNode.value.equals(val)) {
            return true;
        }
        else if (val > rootNode.value) {
            //traverse right
            if (rootNode.right == null) {
                return false;
            }
            return _walkCheck(rootNode.right, val);
        }
       else if (val < rootNode.value) {
            //traverse left
            if (rootNode.left == null) {
                return false;
            }
            return _walkCheck(rootNode.left, val);
        }
        return false;

    }

    @Override
    public String toString() {
        return "BinarySearchTree{" +
            "root=" + root +
            '}';
    }
}

