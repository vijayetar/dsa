package data_structures.stacksAndQueues;

public class Node<T> {
    T value;
    Node<T> next;
    public Node(T value){
        this.value = value;
    }
    public Node(T value, Node<T> next){
        this.value = value;
        this.next = next;
    }
    public Node(){
        this.value = null;
    }
    public String toString(){
        return String.format("{%s}",this.value);
    }
    public T getValue(){
        return this.value;
    }
}
