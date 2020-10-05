# GROKKING THE CODING INTERVIEW

## Sliding Window
*  find the average of all contiguous subarrays of size k
    * by using the sliding window technique where you are adding the next value and removing the first value in the subwindow, the time efficiency is O(n)
    * otherwise if you recalculated the sum with each iteration, then the efficiency is O(n*k)
*  find the maximum sum of the all contiguous subarrays of size k
    * Define function that takes in an array and an integer k
    * Determine the sum of the first k numbers
    * Set a variable max to the first sum
    * Now slide over the array until the end (length of array – k +1)
    * Reassign the max to the sum if the sum > max
    * Return the max number


## References
[Negative infinity as float('-inf')](https://www.geeksforgeeks.org/python-infinity/)
