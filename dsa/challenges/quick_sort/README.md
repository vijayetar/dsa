# Quick Sort

[Table of Contents](../../../README.md)

See [solution](quick_sort.py)

__PR__:https://github.com/vijayetar/dsa/pull/22

## Challenge
Review the pseudocode below, then trace the __algorithm__ by stepping through the process with the provided sample array. __Document your explanation__ by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

## Pseudocode
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

## Approach and Efficiency
[doc-file]()

The approach in the worst case scenario where the pivot is an extreme end of the array, either smallest or largest, the worst scenario is O(n^2).

In the average cases, where the we choose a pivot value that is median of the array, the efficiency is O(nlogn)

And in the best case, where the list is already sorted in ascending order, it would be O(n) only.

The space is only O(n) since a new array is not created.

## Specifications Used
* .editorconfig
* .gitattributes
* .gitignore

## Solution
![page1](../../assets/quicksort1.png)
![page2](../../assets/quicksort2.png)

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
