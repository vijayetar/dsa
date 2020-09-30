package data_structures.stacksAndQueues;
import data_structures.stacksAndQueues.Node;
import java.util.ArrayList;
import java.util.EmptyStackException;

public class Queue<T>{
    private Node<T> front=null;
    private Node<T> rear = null;

    // checks if the stack is empty
    public boolean isEmpty(){
        return front==null;
    }

    // get Front of the Stack
    public Node<T> getFront(){
        return front;
    }


    // returns the value of the top of the Stack
    public T peek () throws EmptyStackException {
        if (isEmpty()) {throw new EmptyStackException();}
        return (T) front.value;
    }


    //     add values to the front of the queue
    public void enqueue(T val){
        Node<T> newNode = new Node(val);
        if (isEmpty()){
            rear = newNode;
            front = newNode;
            return;
        }
        rear.next = newNode;
        rear = newNode;
    }
    public void enqueue (ArrayList<T> values){
        int i = 0;
        if (isEmpty()){
            Node<T> newNode = new Node<T>(values.get(i));
            front = newNode;
            rear = newNode;
            i = 1;
        }
        for (int j = i; j<values.size(); j++){
            Node<T> newNode = new Node<T>(values.get(j));
            rear.next = newNode;
            rear = newNode;
        }
    }
    // remove the front of the queueu
    public T dequeue() throws EmptyStackException {
        if (front == null){
            throw new EmptyStackException();
        }
        Node<T> temp = front;
        front = temp.next;
        return temp.value;
    }
    public String toString(){
        String output = "";
        Node<T> current = front;
        while(current != null){
            output += String.format(current.toString() + " => ");
            current = current.next;
        }
        return output+"NULL";
    }


}
