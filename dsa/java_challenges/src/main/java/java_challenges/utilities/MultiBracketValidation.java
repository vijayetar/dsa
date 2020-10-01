package java_challenges.utilities;

import data_structures.linkedList.LinkedList;

import java.util.EmptyStackException;
import java.util.HashMap;

public class MultiBracketValidation {
    //create Node class with char
    protected static class Node {
        char value;
        Node next;
        public Node (char val){
            this.value = val;
            this.next = null;
        }
        public Node (char val, Node next){
            this.value = val;
            this.next = next;
        }
    }
    //create a stack class
    protected static class Stack {
        Node top = null;
        public boolean isEmpty(){
            return top==null;
        }
        public char peek () throws EmptyStackException {
            if (isEmpty()) {throw new EmptyStackException();}
            return top.value;
        }
        public void push(char val){
            Node newNode = new Node(val);
            if (isEmpty()){
                top = newNode;
                return;
            }
            top = new Node(val, top);
        }
        public char pop() throws EmptyStackException {
            if (top == null){
                throw new EmptyStackException();
            }
            Node temp = top;
            top = top.next;
            return temp.value;
        }
    }

    //make a stack and then check each bracket and then close it and pop it off
    // and if it is empty then we will return true
    public static boolean multiBracketValidationWithString (String inputString){
        System.out.println("this is the inputString "+inputString);
        //create a hashmap of the brackets with O1 look up time
        // instantiate a stack
        // iterate over the string and then add to the stack as we see
        HashMap<Character, Character> brackets = new HashMap<>();
        brackets.put('{','}');
        brackets.put('(',')');
        brackets.put('[',']');
        System.out.println("this is the hashmap  "+ brackets);
        Stack bracketStack= new Stack();
        int counter = 0;
        //iterate over the string and get the contents of the string
        // check if it matches the keys in the brackets and then ad it to the stack
        for (int i = 0; i< inputString.length(); i++){
            if (brackets.containsKey(inputString.charAt(i))){
                bracketStack.push(brackets.get(inputString.charAt(i)));
                counter ++;
                //check if the character is a closing bracket
            } else if (brackets.containsValue(inputString.charAt(i))){
                if (bracketStack.isEmpty()){return false;}
                //check if that character is in the Stack
                if (bracketStack.peek() == inputString.charAt(i)) {
                    bracketStack.pop();
                }
            }
        }
        if (bracketStack.isEmpty() && counter!=0){
            return true;
        }
        return false;
    }
}
