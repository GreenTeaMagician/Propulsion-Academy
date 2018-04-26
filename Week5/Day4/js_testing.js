// function myFunction() {
//     var fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
//     var citrus = fruits.slice();
//     return citrus
// }

// console.log(myFunction())

var createMultiplier = function(num) {
    return function(num2) {
      return num * num2;
    }
  }
  
var multiplyByFive = createMultiplier(5);
  
console.log(multiplyByFive(4)); // 20;

//Non curried
var multiplyFour = function (num1, num2, num3, num4) {
    return num1 * num2 * num3 * num4;
  }
  
  multiplyFour(3, 5, 6, 2);

//Curryied. Yum!
var curry = require('curry'); // assume that `curry` comes from a library

var curriedMultiplier = curry(multiplyFour); // `curry` expects a function as parameter
// it returns the curried version of that function

var partialMult = curriedMultiplier(3, 5);

partialMult(6, 2);
