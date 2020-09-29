package data_structures.stacksAndQueues;

public class Node {
    public Integer value;
    public Node next;

    public Node(Integer value){
        this.value = value;
    }
    public Node(Integer value, Node next){
        this.value = value;
        this.next = next;
    }
    public Node(){
        this.value = null;
    }
    public String toString(){
        return String.format("{%s}",this.value);
    }
    public Integer getValue(){
        return this.value;
    }
}
