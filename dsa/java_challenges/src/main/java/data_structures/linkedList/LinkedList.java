package data_structures.linkedList;

public class LinkedList {

        private Node head;
        private Node tail;

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

        // append to the end of the LL in O(1)
        public void append(int newVal){
            if (this.head == null){
                this.insert(newVal);
            }
            else {
                Node newNode = new Node(newVal);
                this.tail.next = newNode;
                this.tail = newNode;
            }
        }

        // inserts a new value AFTER the value given
        public String insertAfter(int val, int newVal){
               Node current = this.head;
               Node newNode = new Node(newVal);
               while (current != null) {
                   if (current.value == val){
                       Node temp = current.next;
                       newNode.next = temp;
                       current.next = newNode;
                       if (this.head==this.tail) {
                           this.tail = this.head.next;
                       }
                       return this.toString();
                   }
                   current = current.next;
               }
               return "value not in linked list";

        }

        // inserts a new value BEFORE the value given
        public String insertBefore(int val, int newVal){
            Node current = this.head;
            Node newNode = new Node(newVal);
            if (this.head.value==val){
                newNode.next = this.head;
                this.head=newNode;
                return this.toString();
            }
            while (current.next != null) {
                if (current.next.value == val){
                    Node temp = current.next;
                    newNode.next = temp;
                    current.next = newNode;
                    return this.toString();
                }
                current = current.next;
            }
            return "value not in linked list";

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
            Node current = this.head;
            Node slower = this.head;
            int counter = 0;
            int slowerNum = k;
            if (k<0){
                slowerNum = 1;
                while (current!= null){
                    if (slowerNum == k*-1){
                        return current.value;
                    }
                    current = current.next;
                    slowerNum ++;
                }
            }
            while (current != null){
                if (counter > slowerNum){
                    slower = slower.next;
                }
                current = current.next;
                counter ++;
            }
            if (counter<slowerNum){
                throw new Exception("It looks like the linked list is too short!");
            }
            return slower.value;
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
        public Node getHead(){
            return this.head;
        }
        public Node getTail(){
            return this.tail;
        }
}

