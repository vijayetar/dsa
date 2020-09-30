package data_structures.stacksAndQueues;

import java.util.EmptyStackException;

public class PseudoQueue <T> {
    //uses the slinky method
    //create a stack 1 for enqueue and stack 2 for dequeue
    Stack<T> enqueueStack = new Stack<>();
    Stack<T> dequeueStack = new Stack<>();
    // adds value to the top of the stack (ie back of the queue)
    public void enqueue(T val) throws EmptyStackException{
        if (enqueueStack.isEmpty()) {
            //take it out of the dequeue Stack and put it into the EnqueueStack
            shuffleStack(dequeueStack, enqueueStack);
        }
        enqueueStack.push(val);
    }
    //pops values from the from the top of the dequeue stack or front of the queue
    public T dequeue() throws EmptyStackException{
        if (dequeueStack.isEmpty()){
            shuffleStack(enqueueStack, dequeueStack);
        }
        return dequeueStack.pop();
    }
    // this shuffles the stacks
    private void shuffleStack(Stack<T> fromStack, Stack<T>toStack){
        Node<T> current = fromStack.top;
        while (current != null){
            toStack.push(fromStack.pop());
            current = fromStack.top;
        }
    }
    // returns a boolean if both stacks are empty
    public boolean isEmpty(){
        return enqueueStack.isEmpty()&& dequeueStack.isEmpty();
    }
    // returns the value at the front of the queue
    public T peek() throws EmptyStackException{
        if (isEmpty()){
            throw new EmptyStackException();
        }
        if (dequeueStack.isEmpty()){
            shuffleStack(enqueueStack, dequeueStack);
        }
        return dequeueStack.top.value;
    }
    public String toString(){
        String output = "";
        if (!isEmpty()) {
            if (dequeueStack.isEmpty()) {
                shuffleStack(enqueueStack, dequeueStack);
            }
            return dequeueStack.toString();
        }
        return output+"Null";


    }
}
