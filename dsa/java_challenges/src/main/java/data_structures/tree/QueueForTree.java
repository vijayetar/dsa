package data_structures.tree;

import data_structures.stacksAndQueues.Node;

import java.util.EmptyStackException;

public class QueueForTree <T>{
    private Node<T> front=null;
    private Node<T> rear = null;

    // checks if the stack is empty
    public boolean isEmpty(){
        return front==null;
    }
    // returns the value of the top of the Stack
    public T peek () throws EmptyStackException {
        if (isEmpty()) {throw new EmptyStackException();}
        return front.getValue();
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
    // remove the front of the queueu
    public T dequeue() throws EmptyStackException {
        if (front == null){
            throw new EmptyStackException();
        }
        Node<T> temp = front;
        front = temp.next;
        return temp.getValue();
    }

}
