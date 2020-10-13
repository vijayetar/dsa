# GROKKING THE CODING INTERVIEW

## Sliding Window
* 1.1  find the average of all contiguous subarrays of size k
    * by using the sliding window technique where you are adding the next value and removing the first value in the subwindow, the time efficiency is O(n)
    * otherwise if you recalculated the sum with each iteration, then the efficiency is O(n*k)
* 1.2  find the maximum sum of the all contiguous subarrays of size k
    * Define function that takes in an array and an integer k
    * Determine the sum of the first k numbers
    * Set a variable max to the first sum
    * Now slide over the array until the end (length of array – k +1)
    * Reassign the max to the sum if the sum > max
    * Return the max number
* 1.3 Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

    * Define a function that takes in an array and a number
    * expand the subarrays starting from 1, expand by 1 to the length of the array
    * stop expanding as soon as sum is same  or greater than k
    * have variable called lower length and assign it to the lowest length
    * return the length of the lowest number

* 1.4 Given a string, find the length of the longest substring in it with no more than K distinct characters.

*1.6 Given a string, find the length of the longest substring which has no repeating characters.

## References
[Negative infinity as float('-inf')](https://www.geeksforgeeks.org/python-infinity/)
