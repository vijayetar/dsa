package data_structures.stacksAndQueues;

public class Node {
    public int value;
    public data_structures.linkedList.Node next;

    public Node(int value){
        this.value = value;
    }
    public String toString(){
        return String.format("{%s}",this.value);
    }
}
