# Linked List

[Table of Contents](./../../../../../../README.md)

## Challenge
Linked List created with the following methods:
__addToFront(int n)__ :method that takes in parameter integer and adds it to the front of the linked List and moves the head to the front. It uses O(1)approach for space and time;
__addToEnd(int newVal)__: method that takes in a new value and appends it to the tail of the linked list in O(1) approach.
__kthFromTheEnd(int val)__: method that takes in an integer and finds the kth value from the end.  It will return the end at k=0, and throw exception if the k>length of the linked list.
__isEmpty__ returns a boolean if the linked list is empty with O(1) time approach
__includes(int n)__:method that iterates through the linked list to check if the value n is present in the linked list.  This uses a O(n) time efficiency.

## Approach and Efficiency
__includes(int n)__: time O(n), space O(1)
__isEmpty()__: O(1)
__addToFront(int n)__: time O(1), space O(1)
__addToEnd(int n)__: time O(1), space O(1)
__kthFromTheNode(int val)__: time O(n), space O(1)

## Specifications Used
* .editorconfig
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
