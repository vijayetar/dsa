package data_structures.stacksAndQueues;

import data_structures.linkedList.Node;

public class Stack{
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
    // get Top of the Stack
    public Node getTop(){
        return top;
    }
    // returns the value of the top of the Stack
    public int peek() throws Exception {
        if (top==null){
            throw new Exception("Stack is empty");
        }
        return top.value;
    }
//     add values to the top of the stack
    public void push(Integer val){
        if (isEmpty()){
            top = new Node(val);
            return;
        }
        top = new Node (val, top);
    }
    public void push (int[] values){
        int i = 0;
        if (isEmpty()){
            top = new Node(values[i], top);
            i = 1;
        }
        for (int j = i; j<values.length; j++){
            top = new Node(values[j], top);
        }
    }
    // remove the top of the Stack
    public Integer pop(){
        Node temp = top;
        top = top.next;
        return temp.value;
    }
    public String toString(){
        String output = "";
        Node current = top;
        while(current != null){
            output += String.format("{%d}=> ", current.value);
            current = current.next;
        }
        return output+"NULL";
    }

}
