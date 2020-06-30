# Get_edge_graph

[Table of Contents](../../../README.md)

See [solution](get_edge.py)

__PR__:https://github.com/vijayetar/dsa/pull/31

## Challenge
Write a function based on the specifications above, which takes in a graph, and an array of city names. Without utilizing any of the built-in methods available to your language, return whether the full trip is possible with direct flights, and how much it would cost.

## Approach and Efficiency
This looks like O1 efficiency to check if the origin exists in the graph, then find the neighbors.
there is a loop through the neighbors that is variable O(n) that is not correlated to the size of the graph, but worst case scenario it is O(n)
and then once the matching destination is found, a boolean is returned with the weight.

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore


## Solution
![whiteboard](../../assets/graph_destination.png
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
