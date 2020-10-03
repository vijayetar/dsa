package java_challenges.utilities;

import data_structures.stacksAndQueues.Queue;

import java.util.EmptyStackException;

public class DuckDuckGoose {
    // write  a method that takes in a queue of strings and an integer k and removes the kth value until only one string  is left and return the string
    public String ddG(Queue<String> q, int k) throws EmptyStackException {
        //check for empty q
        if (q.isEmpty()){throw new EmptyStackException();}
        // checks k is >0
        if (k<1){throw new IllegalArgumentException("Cannot enter 0 or less than 0");}
        return _play(q, 0, k);

    }
    private String _play(Queue<String> q, int counter, int k){
        if (q.getFront().next == null){return q.dequeue();}
        counter ++;
        if (counter == k){
            q.dequeue();
            return _play(q,0,k);
        }
        if (counter<k){
            q.enqueue(q.dequeue());
        }
        return _play(q,counter,k);
    }
}
