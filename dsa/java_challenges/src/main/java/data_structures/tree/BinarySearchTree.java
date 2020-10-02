package data_structures.tree;

public class BinarySearchTree<T> extends Tree<T> {
    public BinarySearchTree() {
    }

    public BinarySearchTree(NodeTree<T> rootNode) {
        super(rootNode);
    }
    @Override
    public void add(NodeTree<T> newNode){
        if (this.root == null){this.root = newNode; return;}
        _walk(this.root, newNode);
        return;
    }
    @Override
    private void _walk(NodeTree<T> current, NodeTree<T> newNode){
        System.out.println("here are the values:  " + current.value + newNode.value);
        if (current.value == newNode.value){
            if (current.left != null){
                _walk(current.left, newNode);
            } else {
                current.left = newNode;
                return;
            }
        }
//        else {
//            if (current.right != null){
//                _walk(current.right, newNode);
//            } else {
//                current.right = newNode;
//                return;
//            }
//        }
    }
}
