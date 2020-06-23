# Binary Tree Intersection

[Table of Contents](../../../README.md)

See [solution](tree_intersection.py)

__PR__:https://github.com/vijayetar/dsa/compare/tree-intersection?expand=1

## Challenge
* Write a function called tree_intersection that takes two binary tree parameters.
* Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

## Approach and Efficiency
This is not an efficient way to check for the presence of nodes in tree.
I have to use at least one O(n) to traverse the first tree with depth traversal, and create a bt_list.
Then as I traverse the second tree, i can check if th value exists in the bt_list and if it does, then append it to a new returned list.
In situation it is O(n^2).
And since I am also checking each value of the tree node with the created list, it is O(n) each time as well.
WRT space, I create two lists at least, and that takes up space.

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore


## Solution
![whiteboard](../../assets/tree_intersection.png
)

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
