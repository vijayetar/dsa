package data_structures.stacksAndQueues;

import java.util.EmptyStackException;

public class Stack<T>{
    private Node<T> top = null;

    // checks if the stack is empty
    public boolean isEmpty(){
        return top==null;
    }


    // get Top of the Stack
    public Node<T> getTop(){
        return top;
    }


    // returns the value of the top of the Stack
    public T peek() throws EmptyStackException {
        return isEmpty()? null: top.value;
    }


//     add values to the top of the stack
    public void push(T val){
        Node<T> newNode = new Node(val);
        if (isEmpty()){
            top = newNode;
            return;
        }
        top = new Node<T>(val, top);
    }
    public void push (T[] values){
        int i = 0;
        if (isEmpty()){
            top = new Node<T>(values[i], top);
            i = 1;
        }
        for (int j = i; j<values.length; j++){
            top = new Node<T>(values[j], top);
        }
    }
    // remove the top of the Stack
    public T pop() throws EmptyStackException {
        if (top == null){
            throw new EmptyStackException();
        }
        Node<T> temp = top;
        top = top.next;
        return temp.value;
    }
    public String toString(){
        String output = "";
        Node<T> current = top;
        while(current != null){
            output += String.format("{%d}=> ", current.value);
            current = current.next;
        }
        return output+"NULL";
    }

}
