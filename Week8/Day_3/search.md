# Advanced algorithms - search

Alright, let's start with a seemingly simple programming task. 

> In a list `L` of `n` elements, find the position of an item that matches the query value `query` and return its position within the array. If the element cannot be found, return `-1` 

The most straight-forward approach could be the following: Start at the beginning of the list & sequentially examine every single item in the list - until you either found the element or you reached the end. Or in Javascript that would be:
```Javascript
function findMax(arr) {
  for (var i=0; i<arr.length; i++) {
    if (arr[i] == value)
      return i;
  }

  return -1;
}
```
Let's start analyzing this algorithm. Runtime? Iterate through the array once, examine each element once -> looks like `O(n)` in runtime. Space complexity? Actually none, so `O(1)`.

Not bad, right? This algorithm actually has a name: the *linear search* or *sequential search*. Actually, it is the best solution that you can do with an arbitrary array. It seems so obvious, why bother? In the next section you will see if we can do better, provided we can make some assumptions.

### Search on a sorted list.

Let's modify the precondition on the input slightly:
> In a list `L` of `n` **sorted integer** elements, where `L(i) <= L(i-1)` , find  the position of an item that matches the query value `query` and return its position within the array. If the element cannot be found, return `-1`.

See what we did there? The assumption of the *sorted number array* allows for some clever optimizations compared to the linear search.

Assume you start with the element from the middle of the array. If you found the element in question, then you're done. If the element in the middle of the array is larger than the one you are searching for, then that must mean that the `query` item is in the first half of the array. If the element in the middle is smaller, then the `query` item must be in the second half of the array. You probably guessed it right - we just repeat the same procedure in that part of the array where your element must be over and over again, recursively, until you are either left with only one element or you found your `query` element. 

The following image illustrates this algorithm in more visual detail:

![Binary search illustrated](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Binary_Search_Depiction.svg/470px-Binary_Search_Depiction.svg.png)

But is it better than the linear search? After all it sounds more complicated than just iterating through the whole list. Let's analyze its behavior. We start by looking at element in the middle of the array, i.e. at index `n/2` and make one comparison. Depending on the comparison we look either left or right. For the sake of simplicity, let's assume the element in question is in the lower half of the array. We therefore get the element at position `n/4`, and make one comparison again. And we repeat that process again and again, at positions `n/8`, `n/16`, `n/32`, and so on, until we found the element or arrived at index position `0`. 

So what does this mean? At each step, we reduce the space to search by a factor of `1/2`, and at most we will have to look at `O(log n)` elements to determine wheter or not the element in question can be found in the array. Amazing! Compared to the linear search that runs in `O(n)`, we just reduced the amount of searching dramatically. For say, 100 million sorted elements, you now can find a match in less than 27 steps Compare this to the worst case scenario for linear search, where you need to look at 100 million elements.

(If you are unsure why `log n`, maybe check the [Wikipedia page on binary logarithms](https://en.wikipedia.org/wiki/Binary_logarithm))

This algorithm is called **binary search**, and was one of the first computer science algorithms ever invented, dating [back all the way to 1946](https://en.wikipedia.org/wiki/Binary_search_algorithm#History).
 
### Binary search algorithm

* **PROBLEM**: Given a list of sorted integers, find index of query value
* **INPUT**: List `L` of `n` numbers, query item `q`
* **OUTPUT**: Index `i` of `q` in `L`. Return `i=-1` if it doesn't exist.
* **ALGORITHM**: `binarySearch(L, q)`
  1. If `n == 0`, then we haven't found the element -> `return -1`
  1. If `L[n/2] == q`, return `n/2`
  1. If `L[n/2] > q`, then search in lower half of array, i.e. `return binarySearch(L[0...n/2])`
  1. If `L[n/2] < q`, then search in upper half of array, i.e. `return binarySearch(L[n/2...n])`
## Further reading

* [Wikipedia on binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm)
