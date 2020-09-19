package data_structures.linkedList;

import javax.lang.model.type.NullType;

public class LinkedList {

        public Node head;
        public Node tail;

        // inserts the node to the head of the linked list
        public void insert(int n){
            Node newNode = new Node(n);
            if (this.head == null){
                this.head = newNode;
                this.tail = newNode;
            } else {
                newNode.next = this.head;
                this.head = newNode;
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
            } else return "The Linked List is empty";
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
}

