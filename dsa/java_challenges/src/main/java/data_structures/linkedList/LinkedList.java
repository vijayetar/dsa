package data_structures.linkedList;

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
                throw new IndexOutOfBoundsException("It looks like the linked list is too short!");
            }
            return slower.value;
        }

        // returns a string of values within the linked list
        public String toString(){
            return toString(head);
        }

        private String toString(Node current){
            if (current == null) {return "NULL";}
            String output = String.format("{%d} => ",current.value) + toString(current.next);
            return  output;
        }

        public Node getHead(){
            return this.head;
        }
        public Node getTail(){
            return this.tail;
        }
        // static method to zip two linkedLists given as arguments
        public static LinkedList zipLists(LinkedList ll1, LinkedList ll2) throws Exception {
            if (ll1.head == null & ll2.head==null){
                throw new Exception("Both linked lists are empty!");
            }
            if (ll1.head == null) {return ll2;}
            else if (ll2.head == null) {return ll1;}
            Node current1 = ll1.head;
            Node current2 = ll2.head;
            Node temp1 = current1.next;
            Node temp2 = current2.next;
            while (temp1 !=null & temp2 != null){
                current1.next = current2;
                current2.next = temp1;
                current1 = temp1;
                current2 = temp2;
                temp1 = temp1.next;
                temp2 = temp2.next;
            }
            current1.next = current2;
            if (temp1 !=null & temp2 ==null){
                current2.next = temp1;
            }
            return ll1;
        }
//        public static LinkedList zipLists(LinkedList ll1, LinkedList ll2) throws Exception {
//            if (ll1.head == null & ll2.head==null){
//                throw new Exception("No LLs");
//            }
//            return LinkedList.zipLists(ll1.head, ll2.head);
//        }
//        private static LinkedList zipLists(Node current1, Node current2) throws Exception {
//            if (current1 == null) {
//                return current2;
//            }
//            Node temp = current1.next;
//            current1.next = current2;
//            current1 = current2;
//            return LinkedList.zipLists(current1, temp);
//        }
        public static int 


}

