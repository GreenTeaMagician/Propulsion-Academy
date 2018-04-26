# Space-time complexity

Algorithms should not only perform their given task correctly, but they should also perform their task efficiently. In this lesson, we will show you how to analyze if an algorithm is efficient both in run-time and memory usage. To achive this, we introduce the big-O notation for space and time complexity, and show you how this can be used to compare different algorithms.

## Intro to complexity

Algorithms usually take longer the larger the input data. As such, we really want to characterize an algorithm by its complexity *in relation to the input size*. If we want to run `findMax` on an array 10 times larger, how does the overall runtime change? Will it take twice as long, 10 times longer, or even 100 times longer?

Algorithmic complexity could be measured as a numerical function `T(n)`, the time `T` it takes to complete a task on an input of the size `n`. However, `T(n)` depends on the algorithm, its implementation, the processor it runs on, the disk speed, and so on. Or put differently - an algorithm might run faster on your laptop than on your smartphone.

To solve that problem, efficiency is usually measured *asymptotically*. This is one of the fundamental ideas of computer science: instead of using time as the measuring factor, an algorithm is characterized by the number of elementary **"steps"** it takes to complete the task. This allows to abstract away details and classify run-time based on the input size in a platform-independent way. An elementary step is defined as a step that can be completed in constant time - for example the addition of two numbers, or a memory lookup.

Let's apply this to practice and start with the analysis of our algorithm from the last lesson:
```Javascript
// Given a list of 'n' positive numbers, find the largest one
function findMax(array) {
  var maxVal = 0;
  for (var x of array) {
    if (x > maxVal)
      maxVal = x;
  }
  return maxVal;
}
```
So, how many operations happen here? 
1. `maxVal` is initialized. This is **1 operation**.
2. Each value `x` is taken out of the array of length `n`. Taking out one value is 1 operation, taking out all values will be **n operations**.
3. Each value `x` will be compared against `maxVal`. Again, one comparison is 1 operation, and in total **n operations**.
4. If `x` is the new maximum, then this value needs to be stored in `maxVal`. But how often will that happen? This obviously depends on the input. In the best case the highest value is at the beginning of the array, and we only need to compare one element, i.e. **1 operation**. In the worst case the array contains sorted values, starting with the value `1` and ending with the highest value `n`, then this replacement happen `n` times, and take **n operations**. 
5. At the end, one value is returned - this will take another **1 operation**

Let's sum all of this up. In the best case, when the highest element is at the beginning, the overall complexity will be

> T(n) = 3+2*n

In the worst case, when the array is already sorted, the overall complexity will be:

> T(n) = 2+3*n

In practice, complexity is usually given by the worst-case input which results in the longest runtime. So, in a nutshell, `findMax` has a worst-case runtime of `2+3*n`.

So far, we neglected another important factor in complexity analysis - that is the memory consumption. In our `findMax`, we luckily don't need much storage. The only additional storage is `maxVal`, which keeps the current maximum value. As such, the memory requirements of our algorithm are just `M(n) = 1`.

As mentioned earlier: depending on the platform on which the algorithm runs on, the run-time will be different. However, `T(n)` shows that the time grows linearly with the input size. In other words, if the length of the array doubles, then the time to find the max element also approximately doubles. And that is the beauty of assymptotic run-time analysis - the runtime will always double, regardless if the algorithm runs on an old Gameboy or on a supercomputer.

## The big-O notation

Our previous analysis was very detailed. However, the run-time of algorithms is usually not described in such detail. A more common notation is the big-O notation, which is written in the form of `O(n)`. Big-O is designed to highlights the most influential factor on runtime only. In other words, when writing in the big-O notation, we only keep the fastest-growing term and drop all the other slower-growing terms. 

Applied to our `findMax` algorithm, instead of writing `O(2+3n)` we drop all the lower terms and only write `O(n)`. The smaller terms don’t contribute that much to the growth of the function as the input size `n` increases. If `n` increases by a factor of 100, the n term increases the work by a factor of 100. The influence of the `+2` additional elements and the `3x` become insignificant compared to the increase of the factor `100`.

Some of the most common complexities for algorithms are (increasing in complexity):
* `O(1)`: contant time complexity. The number of operations for an algorithm doesn't change as the problem size increases.
* `O(log n)`: logarithmic complexity with the base 2. Algorithms with logarithmic complexity usually are pretty awesome and can cope very well with large data sets. Doubling the input size requires only a constant number of new operations. An input set of size 32 will require `log(32)=5` operations, and an input set of size 1204 will require `log(1024)=10` operations. In other words, for an input set that is 32 times larger, the algorithm will only need 5 more operation. Pretty sweet.
* `O(n)`: linear complexity. Doubling the input size also doubles the number of required operations. Pretty good.
* `O(n log n)`: quasiliner complexity. Doubling input size doubles number of required operations + one operation. Not bad, but not as as good as linear complexity.
* `O(n^2)`: quadratic complexity. Doubling the input set multiplies the operation count by four. A problem 10 times larger takes 100 times more work. Not that great.
* `O(n^3)`, `O(n^4)`, ...: polynomial complexity. Even less great.
* `O(2^n)`: exponential complexity. Increasing the input set by just one element doubles the work. Making the input set twice as big, makes the work 4 times complex. Basically the work increases so quickly, that you can only apply these kind of algorithms to very small input sets in a feasible amount of time. Very bad, for obvious reasons.

The following picture illustrates the effects of the different complexities. The number of input elements `n` is increasing along the x-axis, whereas the y-axis shows the increase in number of operations `N`: 
![Big Oh Notation illustrated](https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison_computational_complexity.svg)

Note that the big-O notation is always an upper bound on run-time, i.e. describes the run-time for the worst-case scenario. Other inputs may let the algorithm run more quickly. For example, an algorithm to search for a particular item in a list may be lucky and find a match on the very first item it tries. The work required in the best-case speed may therefore be much less than that required in the worst case. For such cases, there also exists the Omega notation that describes the best case. However, we are usually interested in the worst case, and we won't go into detail for Omega.

#### What's next?

Now that you have a good overview on algorithms and their complexity, let's start by introducing a couple of fundamental algorithms and their complexity in the following lessons. Let's start with [searching in arrays](./search.md).
