# Introduction to Algorithms

Let's start with Wikipedia's definition again:

> In mathematics and computer science, an algorithm is an unambiguous specification of how to solve a class of problems. Algorithms can perform calculation, data processing and automated reasoning tasks.

Simply put, an algorithm is a series of contained steps that you follow to solve a problem or to achieve a goal. Algorithms have been around almost as long as mathematics, but they are mostly used in the context of computer science.

I some sense, your grandma's recipes are very similar to algorithms: Heat the oven up to 200 degrees. Mix 500g flour, 1 tbsp of salt, 2 tbsp of baking powder. Add 5 eggs and 100ml of milk, and whisk until fully mixed. Pour into a form, put it into the oven, and bake  about 15 minutes until it is fully done.

However, there are some differences from algorithms to classical recipes. The following properties make an algorithm an algorithm:
1. An algorithm is a precise, clear, and most importantly, a **unambiguous** specificiation of how to implement the algorithm. Grandma's recipes are often very unclear - and what means fully baked exactly? We have all been there. More precise would be "until the batter has fully coagulated, and a knife poked into the cake comes back clean." (Yes, I also had to Google "coagulated")
1. An algorithm expects a clearly defined set of inputs. For example, a square root function requires one number greater than zero as input, a sorting algorithm might require an array with an arbitrary amount of numbers in it.
1. An algorithm produces a clearly defined output. Your square root function will produce a number, that is the square root of the input, and will produce an error if the input was below zero. The sorting function will return an array, that contains all elements from the input and where each element in the array is smaller than its following neighbour.
1. An algorithm always terminates, i.e. stops in a finite amount of time. An algorithm that runs forever and never gives a result isn't particulary useful.
1. An algorithm always gives back the correct result. After all, you want to rely on it.
1. If an algorithms requires its input to be of a certain form (e.g. only positive numbers), only then the algorithm is allowed to fail. Requirements on the inputs are also called preconditions.


Enough of this dry matter! Let's have a look at our first algorithm.

#### Example Algorithm: find the largest number in array

Let's define a rather simple algorithm to find the largest number in an array.

* **PROBLEM**: Given a list of positive numbers, find the largest one.
* **INPUT**: List `L` of positive numbers, with at least one number in it.
* **OUTPUT**: A number `n`, which is guaranteed to be the largest from `L`.
* **ALGORITHM**:
  1. Set `maxValue` to `0`.
  1. For each number `x` from list `L`, if `x` is larger than `maxValue` then replace `maxValue` with `x`.
  1. `maxValue` contains now the largest element from list `L`.

So, is this an algorithm? Let's check against our list of specifications:
- [x] It is unambiguous. Each step consists of precisely defined primitive operations. Translating this algorithm to code should be easy.
- [x] Input and output are clearly defined.
- [x] The algorithm always terminates, because lists are always finite.
- [x] The algorithm produces the correct result. (Proofing this is a little bit more complex, can often done with mathematical induction and other methods. But that is beyond the scope here).

Let's translate this into a possible JavaScript implementation:
```Javascript
function findMax(array) {
  var maxVal = 0;
  for (var x of array) {
    if (x > maxVal)
      maxVal = x;
  }
  return maxVal;
}
```

Alright, now that you have a clear idea what an algorithm is, let's move on to the next topic.

#### What's next?

Before we look at some more advanced algorithms, it is important to introduce the concept of space-time complexity. You can find an introduction [in the next lesson](./complexity-intro.md).

 

