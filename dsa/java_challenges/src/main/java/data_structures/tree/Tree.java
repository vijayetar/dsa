package data_structures.tree;

import java.util.ArrayList;
import java.util.EmptyStackException;

public class Tree<T> {
    //variables
    private QueueForTree<NodeTree<T>> rootQueue;
    public NodeTree<T> root;
    private ArrayList<T> listOfNodes;

    // constructors
    public Tree(){this.root = null;}
    public Tree (NodeTree<T> rootNode){
        this.root = rootNode;
    }
    //getters and setters
    public void setRoot(NodeTree<T> node){
        this.root = node;
    }
    public T getRoot(){
        return root.value;
    }
    public boolean isEmpty(){
        return root==null;
    }
    // use breadth traversal to add to the tree
    public void add(NodeTree<T> newNode){
        if (this.root == null) {
            this.root = newNode;
            return;
        }
        rootQueue = new QueueForTree<>();
        this._walk(this.root, newNode);
        //while loop is checking the queue and dequeing and then find the spot where there is null and assign the newNode to that spot
    }
    private void _walk(NodeTree<T> newRoot, NodeTree<T> newNode){
        if (newRoot.left != null){ rootQueue.enqueue(newRoot.left);}
        else {
            newRoot.left = newNode;
            return;
        }
        if (newRoot.right != null){rootQueue.enqueue(newRoot.right);}
        else {
            newRoot.right = newNode;
            return;
        }
        NodeTree<T> temp = rootQueue.dequeue();
        _walk(temp, newNode);
        return;
    }





    // preOrder traversal is grabbing the nodes before you traverse the tree in a depth first manner
    public ArrayList<T> preOrder() throws EmptyStackException{
        listOfNodes = new ArrayList<T>();
        if(!this.root.isNull()){_walkPreOrder(this.root);}
        else {throw new EmptyStackException();}
        return listOfNodes;
    }
    private void _walkPreOrder(NodeTree<T> current){
        listOfNodes.add(current.value);
        if (current.left !=null ) {
            _walkPreOrder(current.left);
        }
        if (current.right != null){
            _walkPreOrder(current.right);
        }
    }





    // inOrder traversal
    public ArrayList<T> inOrder() throws EmptyStackException{
        listOfNodes = new ArrayList<T>();
        if(!this.root.isNull()){_walkInOrder(this.root);}
        else {throw new EmptyStackException();}
        return listOfNodes;
    }
    private void _walkInOrder(NodeTree<T> current){
        if (current.left != null){
            _walkInOrder(current.left);
        }
        listOfNodes.add(current.value);
        if (current.right != null){
            _walkInOrder(current.right);
        }
    }
    // PostOrder traversal
    public ArrayList<T> postOrder() throws EmptyStackException{
        listOfNodes = new ArrayList<T>();
        if(!this.root.isNull()){_walkPostOrder(this.root);}
        else {throw new EmptyStackException();}
        return listOfNodes;
    }
    private void _walkPostOrder(NodeTree<T> current){
        if (current.left != null){
            _walkPostOrder(current.left);
        }
        if (current.right != null){
            _walkPostOrder(current.right);
        }
        listOfNodes.add(current.value);
    }

    @Override
    public String toString() {
        return "Tree{" +
            "root=" + root +
            '}';
    }
}
