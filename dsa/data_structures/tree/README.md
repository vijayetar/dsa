# Tree

[Table of Contents](../../../README.md)

See [solution](tree.py)

__PR__: https://github.com/vijayetar/dsa/pull/14

## Challenge
* Create a __Node class__ with the left child pointing, and the right child poininting to node.
* Create a __BinaryTree class__
* Define a method for each of the depth first traversals called __preOrder, inOrder, and postOrder__ which returns an array of the values, ordered appropriately.
* Any __exceptions or errors that come from your code should be semantic, capturable errors__. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

* Create a __BinarySearchTree class__
* Define a method named __add__ that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
* Define a method named __contains__ that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## Approach and Efficiency


* __Binary Search Tree__:
The Big O time complexity of a Binary Search Tree’s __insertion__ and __search__ operations is O(height). In the worst case, we will have to search all the way down to a leaf, which will require searching through as many nodes as the tree is tall. In a balanced (or “perfect”) tree, the height of the tree is log(n). In an unbalanced tree, the worst case height of the tree is n.

The Big O space complexity of a BST search would be O(1). During a search, we are not allocating any additional space.

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore


## Solution


## Checklist
 - [x] Top-level README “Table of Contents” is updated
 - [ ]  Feature tasks for this challenge are completed
 - [ ] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [ ] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [x] Picture of whiteboard
