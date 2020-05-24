# Linked Lists

[Table of Contents](../../../README.md)

See [solution for class 5, 6 and 7](linked_list.py)

__Pull Request for lab 5__:https://github.com/vijayetar/dsa/pull/3
__Pull Request for lab 6__:https://github.com/vijayetar/dsa/pull/8
__Pull Request for lab 7__:https://github.com/vijayetar/dsa/pull/6

# Challenge for class 5
* Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
* Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
* Define a method called __insert__ which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
Define a method called __includes__ which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
Define a method called __toString__ (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Approach and Efficiency
The approach for this seems straight forward in creating Node class with O(1) function and then a linked list
Since each node points to the next node, they are not stored in the same location. There is definitely more storage efficiency.
WRT to the insert method, it appends at the head, and so it is O(1) as well.
However, the includes method is O(n) since it is dependent on the the length of the linked list.

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore

## Solution
![whiteboard1](../../assets/linked_list1.jpg)
![whiteboard1](../../assets/linked_list2.jpg)

# Challenge for class 6
Write the following methods for the Linked List class:

.append(value) which adds a new node with the given value to the end of the list
.insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
.insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

## Approach and Efficiency
WRT to the append/insertBefore and inserAfter method, given the nature of the singly-linked lists, the code requires us to traverse through the list before locating these positions. This means that the BigO is O(n) since it is dependent on the the length of the linked list.  Since i tried to enter multiple arguments as well, I realized that that there are two loops arguments arg and the linked list n, so the BigO can be increased by the arg size as well as the n factor

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore

## Solution
![whiteboard1](../../assets/linked_list3.jpg)
![whiteboard1](../../assets/linked_list4.jpg)

## Checklist

- [x] Feature Tasks
     - [x] .append(value) which adds a new node with the given value to the end of the list
     - [x] .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
     - [x] .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
- [x] Top-level README “Table of Contents” is updated
- [x] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [x] Picture of whiteboard

# Challenge for class 7
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach and Efficiency
I used O[1] approach to remove negative integers inserted as parameters
Now to get the kth position from the end in a singly linked list, I needed to iterate through the list to get the total number of nodes.  Then if the k value was greater than the length, then a error message was returned.
Then calculating the difference from the length, the positon from the beginning was calculated. Then starting from the head, the (length - k)th position was calculated and returned.

Since the best outcome required two iterations of the loop, the BigO(n) and dependent on the length of the linked list.

time = 2xO(n) = O(n)
space = 1xO(n) = O(n)
## Solution
![whiteboard1](../../assets/linked_list5.jpg)

## Checklist

- [x] Feature Tasks
     - [x]Able to show kth value from end starting at 0
- [x] Top-level README “Table of Contents” is updated
- [x] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [x] Picture of whiteboard
