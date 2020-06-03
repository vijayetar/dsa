# Tree Breadth First

[Table of Contents](../../../README.md)

See [solution](tree_breadth_first.py)

__PR__: https://github.com/vijayetar/dsa/pull/17

## Challenge
* Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

## Approach and Efficiency
I used the breadth traversal with space efficiency of O(h) where h = height in an unbalanced tree, and in the worst case scenario it would be O(n) and in a balanced tree it would be log n. I also create a new list to return.

Time efficiency is O(n)

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore

## Solution
![tree_breadth_1](../../assets/tree_breadth_1.jpg)
![tree_breadth_2](../../assets/tree_breadth_2.jpg)


## Checklist
 - [x] Top-level README “Table of Contents” is updated
 - [x] Feature tasks for this challenge are completed
 - [ ] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [x] Picture of whiteboard
