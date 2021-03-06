# Linked List

[Table of Contents](./../../../../../../README.md)

__PR__:https://github.com/vijayetar/dsa/pull/47

__WhiteBoards__:
### Insert Before   
![InsertBefore](../assets/insertBefore.png)
### Insert After
![InsertAfter](../assets/insertAfter.png)
### Find Kth Node from the end
![kthFromTheNode](../assets/Kth_from_the_end.png)
### Zip Lists
![ZipLists](../assets/LL_zipLists.png)

## Challenge
Linked List created with the following methods:
__insert(int n)__ :method that takes in parameter integer and adds it to the front of the linked List and moves the head to the front. It uses O(1)approach for space and time;
__isEmpty__ returns a boolean if the linked list is empty with O(1) time approach
__includes(int n)__:method that iterates through the linked list to check if the value n is present in the linked list.  This uses a O(n) time efficiency.
__append(int newVal)__: method that takes in a new value and appends it to the tail of the linked list in O(1) approach.

__insertAfter(int val, int newVal)__: method that takes in two integers, and iterates over the entire linked list until the value is found, and inserts a Node of the new value after the current node. It returns a string either of the linked list containing the node or a string "not found" if the node value is not found.

__insertBefore(int val, int newVal)__: method that takes in two integers, and iterates over the entire linked list until the value is found, and inserts a Node of the new value before the current node. It returns a string either of the linked list containing the node or a string "not found" if the node value is not found.

__kthFromTheEnd(int val)__: method that takes in an integer and finds the kth value from the end.  It will return the end at k=0, and throw exception if the k>length of the linked list.

__zipLists(LinkedList ll1, LinkedList ll2)__: STATIC method that takes in two linkedlists as arguments and returns the first linked list with the zipped second linked list

## Approach and Efficiency
__includes(int n)__: time O(n), space O(1)
__isEmpty()__: O(1)
__insert(int n)__: time O(1), space O(1)
__append(int n)__: time O(1), space O(1)
__insertAfter(int val, int newVal)__: time O(n), space O(1)
__insertBefore(int val, int newVal)__: time O(n), space O(1)
__kthFromTheNode(int val)__: time O(n), space O(1)
__zipLists(LinkedList ll1, LinkedList ll2)__: time O(n), space O(1)

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore

## Checklist
 - [x] Top-level README “Table of Contents” is updated
 - [x] Feature tasks for this challenge are completed
 - [x] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [x] Picture of whiteboard
