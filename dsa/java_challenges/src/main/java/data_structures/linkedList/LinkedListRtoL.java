package data_structures.linkedList;

public class LinkedListRtoL {
    public Node head;
    public Node tail;

    // inserts the node to the head of the linked list
    public void addToFront(int n) {
        Node newNode = new Node(n);
        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.head.next = newNode;
            this.head = newNode;
        }
    }

    // returns a string of values within the linked list
    public String toString(){
        if (this.head==null) {return "NULL";}
        Node pointer = this.head;
        String newString = String.format("{%s}",pointer.value);
        while (pointer.next != null){
            newString = String.format("%s => {%s}",newString,pointer.next.value);
            pointer = pointer.next;
        }
        return newString + " => NULL";
    }
    // append to the end of the LL in O(1)
    public void addToEnd(int newVal){
        if (this.head == null){
            this.addToFront(newVal);
        }
        else {
            Node newNode = new Node(newVal);
            newNode.next = this.tail;
            this.tail = newNode;
        }
    }
    // boolean returns if the linked list is empty or not
    public boolean isEmpty(){
        if (this.head == null){return true;}
        return false;
    }

    // returns the value of th head of the linked list
    public String showHead(){
        if (this.head !=null) {
            return String.format("This is the head of the Linked List: : %s",this.head.value);
        }
        return "The Linked List is empty";
    }

    // checks if an inserted value is included in the linked list
    public boolean includes(int n){
        Node pointer = this.head;
        if (pointer == null){
            return false; }
        while (pointer !=null){
            if (pointer.value == n){
                return true;
            }
            pointer = pointer.next;
        }
        return false;
    }
    // finds the value of the node kth from the end, and throws exception if the kth integer is greater than the length of the linked list
    public int kthFromEnd(int k) throws Exception {
        Node current = this.tail;
        int counter = 0;
        while (current != null){
            if (counter == k){return current.value;}
            current = current.next;
            counter ++;
        }
        throw new IndexOutOfBoundsException("It looks like the linked list is too short!");
    }
}
