# Multi Bracket Validation

[Table of Contents](../../../README.md)

See [solution](multi_bracket_validation.py)

__PR__:

## Challenge
Create a function called multi_bracket_validation(input)
Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Approach and Efficiency
I decided to use Stack to create last in and first out to collect the brackets and then make sure that they are closed appropriately. The challenge also was to ensure that they were closed appropriately.  Therefore I had to create a list and a dictionary to match the brackets appropriately and push it into the stack and or pop them only when they matched without using complicated and nested if statements.

Edge cases such as empty string, or string without brackets were also accounted for.

The space and time efficiency is O(n) due to the first for-loop. The pop and push are done with O(1)efficiency. There is a new stack created for this function to work, so takes up space.

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore

## Solution
[Document](https://docs.google.com/document/d/10U1vO309_F5Kvo4IUf1swUJaovXcKByewsZgNB06C4A/edit?usp=sharing)

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
