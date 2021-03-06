#

[Table of Contents](../../../README.md)

See [solution](left_join_hash.py)

__PR__: https://github.com/vijayetar/dsa/pull/29

## Challenge
* Write a function that LEFT JOINs two hashmaps into a single data structure.
* The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
* The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
* Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
* LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
* The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
* Avoid utilizing any of the library methods available to your language.

## Approach and Efficiency
I chosen to use O(n) efficiency to iterate through table1 keys and match it to table 2.  while the matching is O(1), to look for the key is O(m) of table 2 and that will take place the absolute different between sizes of the two tables.

Also, even though the assumption is that retrieval of keys and values is O(1), it can be higher based on collisions in the hashmaps

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore


## Solution
![visual](../../assets/left_join.png)

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
