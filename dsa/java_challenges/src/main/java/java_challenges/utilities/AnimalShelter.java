package java_challenges.utilities;

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

    private static class Node<T> {
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
    public void enqueue(Animal animal){
        if (front == null){
            front = new Node<Animal>(animal);
            rear = front;
        }
        front = new Node<Animal>(animal, front);
    }
    public boolean isEmpty(){
        return front==null;
    }

    public String toString(){
        String output = "";
        if (!isEmpty()) {
            Node<Animal> current = front;
            while(current != null){
                output += String.format("{%s} => ", current.value) + output;
            }
        }
        return output+"NULL";

    }

}
