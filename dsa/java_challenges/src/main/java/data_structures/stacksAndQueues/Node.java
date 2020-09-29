package data_structures.stacksAndQueues;

public class Node {
    public int value;
    public Node next;

    public Node(int value){
        this.value = value;
    }
    public Node(int value, Node next){
        this.value = value;
        this.next = next;
    }
    public String toString(){
        return String.format("{%s}",this.value);
    }
}
