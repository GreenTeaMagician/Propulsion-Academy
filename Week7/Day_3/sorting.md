# Sorting algorithms

In the previous lesson [on searching](./search.md) we learned that we can perform certain tasks much more efficient on sorted lists. In this lesson, we will show you how lists can be sorted.

A sorting algorithm is an algorithm that takes an arbitrary array as input, and returns a sorted version of it. Understanding sorting algorithms helps you to get a good overview of many key concepts in computer science, such as analyzing an algorithm's run-time, divide-and-conquer approaches, and more advanced data structures such as binary trees and heaps. It will not only help you in tackling more challenging problems, but it will also help you during interview processes for jobs - interviewers often like to ask questions related to sorting.

# Algorithm 1: Selection Sort

Selection sort is one of the most straight-forward sorting algorithms. Selection sort searches for the smallest element in the list, and moves that element to the front of the list. This is repeated until the whole list is sorted.

Here is a definition of selection sort:
* **PROBLEM**: Given a list of numbers, return a sorted list.
* **INPUT**: List `L` of `n` numbers, with at least one number in it.
* **OUTPUT**: The same list `L`, but sorted.
* **ALGORITHM**: `selectionSort(L)`
  1. Let `L_unsorted` = `L` be the unsorted portion of the array
  1. Let `L_sorted` = [] be the already sorted portion of the array
  1. While there is still an element in `L_unsorted`:
     1. Find and remove the smallest element of `L_unsorted`
     1. Move the element to the end of `L_sorted` 
  
The algorithm divides the input list into two parts - the portion of the list that is already sorted, which is being built up from front to bottom of the list; and the portion of the list that still needs to be sorted. Initially, the sorted part is empty and the unsorted part is the entire input list. The algorithm proceeds by finding the smallest element in the unsorted sublist, and moving it to end of the sorted list.

### Quick exercise - run-time analysis
Apply the theory you learned into practice - we are looking for the `O()` run-time and memory complexity of this algorithm.


## Algorithm 2: Merge sort

Selection sort is a great first step, but it quickly becomes slow if the array is large. An alternative approach is based on merging already sorted arrays - hence the name merge sort.

Merge sort uses a very common algorithm paradigm called **divide-and-conquer**. Divide an conquer algorithms are always based on the same idea: *divide* the problem in subproblems, *conquer* the subproblems by recursively solving them, and finally combine the solutions of the subproblem to solve the original problem. In order to suceed, each subproblem must be smaller than the original problem, and there must be a "base case" (a smallest problem size) for which the problem becomes simple enough that it can be solved directly.

![Merge sort illustrated](https://en.wikipedia.org/wiki/File:Merge-sort-example-300px.gif)

The idea of the merge sort is to split the input list in half, recursively sort the two halves, and finally merge the two halves together.
* **PROBLEM**: Given a list of numbers, return a sorted list.
* **INPUT**: List `L` of `n` numbers, with at least one number in it.
* **OUTPUT**: The same list `L`, but sorted.
* **ALGORITHM**: `mergeSort(L)`
  1. Solve for first half: `L_sorted_1` = `mergeSort(L[0..n/2])`
  1. Solve for second half: `L_sorted_2` = `mergeSort(L[n/2..n])`
  1. Merge two algorithms: `L = merge(L_sorted_1, L_sorted_2)`

Simple enough! Wait a second, there is still one part missing - merging two arrays
* **PROBLEM**: Given two sorted lists of numbers, return a combined and still sorted list.
* **INPUT**: List `A` and `B` of numbers
* **OUTPUT**: List `L` containing all numbers of `L_1` and `L_2` in sorted order.
* **ALGORITHM**: `merge(A,B)`
  1. Let `L` = [] be the array to return
  1. While there is elements in `L_1` or `L_2`:
     1. If `A[0] < B[0]` then remove `A[0]` and add at end of `L`
     1. If `A[0] >= B[0]` then remove `B[0]` and add at it end of `L`
     1. If `A` is empty, then remove `B[0]` and add at it end of `L`
     1. If `B` is empty, then remove `A[0]` and add at it end of `L`

Alright, interesting algorithm. But is it really faster? Let's find out with the next mini-exercise.

### Quick exercise: run-time analysis
Apply the theory you learned into practice - we are looking for the `O()` run-time and memory complexity of this algorithm.

## More sorting algorithms

We could go on and on about sorting algorithms, but unfortunately there's too many of them. With MergeSort you already learned one of the most important sorting algorithms. Check out [this mesmerizing video that shows 15 sorting algorithms in 6 minutes](https://youtu.be/kPRA0W1kECg)

Here is some additional reading if you want to deep dive into sorting:
* [Wikipedia overview on sorting algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm)

