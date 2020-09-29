package data_structures.stacksAndQueues;

import data_structures.linkedList.Node;

//public class Stack<T> {
//    private Node<T> top = null;
//    public boolean isEmpty () { return top == null; }
//    public T peek() { return isEmpty() ? null : top.value; }
//    public void push(T value) {
//        Node<T> node = new Node(value);
//        if (!isEmpty())
//            node.next = top;
//        top = node;
//    }
//    public T pop() {
//        if (isEmpty()) { return null; }
//        Node<T> node = top;
//        top = top.next;
//        return node.value;
//    }
//}
public class Stack(){
    private Node top;

    public Stack(Node top) {
        this.top = top;
    }
    public Stack(){
        this.top = null;
    }
    // checks if the stack is empty
    public boolean isEmpty(){
        return top==null;
    }
    // returns the value of the top of the Stack
    public int peek() throws Exception {
        if (top==null){
            throw new Exception("Stack is empty");
        }
        return top.value;
    }
    // add values to the top of the stack
//    public void push(int val){
//        Node newVal = new Node(val);
//        if (top == null){
//
//        }
//    }

}
