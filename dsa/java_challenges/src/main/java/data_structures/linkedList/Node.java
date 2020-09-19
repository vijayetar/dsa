package data_structures.linkedList;

public class Node {
    public int value;
    public Node next;

    public Node(int value){
        this.value = value;
    }
    public String toString(){
        return String.format("{%s}",this.value);
    }
}
