package data_structures.tree;

public class NodeTree <T> {
    T value;
    NodeTree<T> left;
    NodeTree<T> right;
    public NodeTree() {
        value = null;
    }
    public NodeTree(T value){
        this.value = value;
    }
    public NodeTree(T value, NodeTree<T> left, NodeTree<T> right){
        this.value = value;
        this.left = left;
        this.right = right;
    }
    public boolean isNull(){
        return value == null;
    }
    public boolean isEmpty(){
        return value == null;
    }

    @Override
    public String toString() {
        return "{" +
            "value=" + value +
            ", left=" + left +
            ", right=" + right +
            '}';
    }
}
