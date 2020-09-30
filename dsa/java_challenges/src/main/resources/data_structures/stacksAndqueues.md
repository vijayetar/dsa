# Stacks and Queues

[Table of Contents](./../../../../../../README.md)
PR: https://github.com/vijayetar/dsa/pull/52


## Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
## Stack
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
__push(int newVal)__:
Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
__pop()__:
Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value in O(1).
Should raise exception when called on empty stack
__peek()__:
Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack O(1)
Should raise exception when called on empty stack
__isEmpty()__:
Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.

## Queue
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
__enqueue(int newVal)__:
Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
__dequeue()__:
Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
Should raise exception when called on empty queue
__peek()__:
Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
Should raise exception when called on empty queue
__isEmpty()__:
Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.  

## Checklist
 - [x] Top-level README “Table of Contents” is updated
 - [x] Feature tasks for this challenge are completed
 - [x] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [NA] Picture of whiteboard
