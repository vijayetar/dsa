package java_challenges.utilities;

import java.util.EmptyStackException;

public class AnimalShelter {
//    Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
//    Implement the following methods:
//    enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
//    dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null
    // create a Cat class
    // create a Dog class
    // create a Other class
    // instantiate them based on the input
    // enqueue them in the queue
//enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
//    dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

    protected static class Node<T> {
        T value;
        AnimalShelter.Node<T> next;

        public Node(T value){
            this.value = value;
        }
        public Node(T value, AnimalShelter.Node<T> next){
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

    Node<Animal> front = null;
    Node<Animal> rear = null;

    // takes each animal either cat or dog or other and adds it to the front of the queue
    public void enqueue(Animal animal) {
        Node<Animal> newNode = new Node<Animal>(animal);
        if (front == null) {
            front = newNode;
            rear = newNode;
        }
        rear.next = newNode;
        rear = newNode;
    }

    public boolean isEmpty(){
        return front==null;
    }

    public Node<Animal> getFront(){
        return front;
    }
//    public String dequeue(Animal animal) {
//        if (isEmpty()){
//            return "null";
//        }
//        Node<Animal> current = front;
//        while(current != null){
//            System.out.println("This is the current in the while loop  "+current.value);
//            System.out.println("HERE ARE WE  " + current.value.getClass().getSimpleName());
//            if (current.value.getClass().getSimpleName().equals(animal.getClass().getSimpleName())){
//                return current.value.toString();
//            }
//            current = current.next;
//        }
//        return "null";
//    }
    public String dequeue(String animal) {
        if (isEmpty()){
            return null;
        }
        Node<Animal> current = front;
        if (current.value.getClass().getSimpleName().toLowerCase().equals(animal)){
            System.out.println("this is front.next "+current.next.toString());
            front = current.next;
            return current.value.toString();
        }
        while(current.next != null){
        System.out.println("This is the current.next in the while loop  "+current.next.value);
        System.out.println("HERE ARE WE  " + current.next.value.getClass().getSimpleName());
        if (current.next.value.getClass().getSimpleName().toLowerCase().equals(animal)){
            Node<Animal> temp = current.next;
            current.next = temp.next;
            return temp.value.toString();
        }
        current = current.next;
        }
        return null;
    }

    public String toString(){
        String output = "";
        Node<Animal> current = front;
        while (current != null){
            output += current.value.toString()+" <= ";
            current = current.next;
        }
        return output+"NULL";
    }


}
