# Linked Lists
####  page 94 from breaking the coding interview

[Answer](practice_linked_lists.py)


#### 2.1 Remove Duplicates from unsorted linked list.  Implement it with and without a temporary buffer

#### 2.3 Find the middle node from the linked list
Both mid and current start at the head, and for every two steps the current pointer advances, the mid pointer advances by 1

#### 2.3b find the middle node and remove it from the linked list

#### 2.4 Given ll, and partition value, use the partition value given and return a linked list with nodes sorted around the partition value

#### 2.5 given two ll with numeric values, return new ll with sum of the values

#### 2.5 alternate
Sum of two linked lists
Inputn:
ll_1 = 2 → 3 → 5 → None
ll_2 = 3 → 6 → 3 → None

Output
235 + 363 = 598
return = 5 → 9 → 8 → None

Algorithm:
1. define function with argument of two linked lists
2. assert both linked lists have a head, and if not, return the other ll
3. convert ll into a string and then into an integer
4. add the two integers
5. convert the sum into a linked list and then return it

#### 2.6 function to check if linked list is a palindrome
* attempt using a temporary buffer such as list and then compare them to each other at either end until middle is reached.
* consider using a stack for first in first out approach until the middle is reached and then compare the rest of the linked list

#### 2.7 function to determine the intersection of linked lists, and return the node with the intersection
* attempt using a hashtable to determine repeats
* if repeat found then traverse the linked list until tail confirmed to be the same and return the matching node
[Whiteboard](https://docs.google.com/document/d/1wnwH7qLnT0Pob2ZNa3RtS1pQ944RagvmM71Fy3p_nEM/edit?usp=sharing)
* another method from the textbook to find the intersection by first finding the shorter of the linked lists and as well as the tail and making sure the tails match
