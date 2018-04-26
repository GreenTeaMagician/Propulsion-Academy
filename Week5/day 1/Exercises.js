var someString = "X-gon give it to ya";
var someArray = ["hit", "me", "baby,", "one", "more", "time!"];
var someObject = { Password: "Swordfish" };

function isString(strOrNah) {
  var type = typeof strOrNah;
  if (type !== "string") {
    return false;
  } else {
    return true;
  }
}

// console.log(isString('hello')); // => true
// console.log(isString(['hello'])); // => false
// console.log(isString('this is a long sentence')); // => true
// console.log(isString({ a: 2 })); // => false

function isArray(arrOrNah) {
  if (arrOrNah instanceof Array) {
    return true;
  } else {
    return false;
  }
}

function areSameType(arrSmeTypeOrNah) {
  var t = typeof arrSmeTypeOrNah[0];
  for (i = 0; i <= arrSmeTypeOrNah.length - 1; i++) {
    if (t !== typeof arrSmeTypeOrNah[i]) {
      return false;
    }
  }
  return true;
}

// console.log(areSameType(['hello', 'world', 'long sentence'])) // => true
// console.log(areSameType([1, 2, 9, 10])) // => true
// console.log(areSameType([['hello'], 'hello', ['bye']])) // => false
// // console.log(areSameType([['hello'], [1, 2, 3], [{ a: 2 }]])) // => true
// s1 = 'thisisthefinalcountdown'
// s2 = 'wearethechampions'
// s3 = 'a'
// function longest(s1, s2)  {
//     var longString = [s1, s2].reduce(function(a,b) {return a.length > b.length ? a : b});
//     var charList = ''
//     for(i = 0; i <= longString.length; i++) {
//         if(charList.indexOf(s1.charAt(i)) <= -1)   {
//             charList += s1.charAt(i)
//         }
//         if(charList.indexOf(s2.charAt(i)) <= -1)   {
//             charList += s2.charAt(i)
//         }
//     }
//     return charList.split('').sort().join('');
// }

// console.log(longest(s1, s2))

// function convert(numOrderPls)   {
//     console.log(numOrderPls)
//     var numArr = String(numOrderPls).split('')
//     console.log(numArr)
//     for(i=0;i<=numArr.length - 1;i++)   {
//         numArr[i] = Number(numArr[i])
//     }
//     console.log(typeof numArr[2])
//     return numArr.sort().reverse()
// }
// // console.log(convert(999977))
// arr = ["hello", "friend", "hello", "asshole"];
// function countArr(howManyDude) {
//   var authors = new Object();
//   for (i = 0; i <= arr.length - 1; i++) {
//     if (arr[i] in authors) {
//       authors[arr[i]] += 1;
// //     } else {
// //       var val = arr[i];
// //       authors[arr[i]] = 1;
// //     }
// //   }
// //   return authors;
// // }

// function isCaught(tomAndJerry) {
//   for (i = 0; i <= tomAndJerry.length; i++) {
//     if (tomAndJerry[i] == "C") {
//       tomIndex = i;
//     }
//     if (tomAndJerry[i] == "m") {
//       jerryIndex = i;
//     }
//   }
//   try   {
//     return Math.abs(jerryIndex - tomIndex) >= 4 ? false : true;
//   }
//   catch(e) {
//       return 'Tom or Jerry not present in string. A sad day indeed...'
//   }
// }
// console.log(isCaught("....C..m"));

// function splitTheBill(maSquadYo) {
//     maSquad = maSquadYo
//     var size = 0
//     var theFortuneWasted = 0
//     for (var key in maSquad) {
//         size++;
//         theFortuneWasted += maSquad[key]
//     }
//     for(var key in maSquad)   {
//         maSquad[key] -= theFortuneWasted/size
//         maSquad[key] = -maSquad[key]
//     }
//     return maSquad
// };

// // function LoopThroughProperties(obj)
// // {
// //     for (var propName in obj)
// //     {
// //         console.log(propName + ": " + obj[propName]);
// //     }
// // }
// var group = {
//   Amy: 20,
//   Bill: 15,
//   Chris: 10
// };

// console.log(splitTheBill(group)); // => { Amy: -5, Bill: 0, Chris: 5 }

// function exp(numba1, othanumba1) {
//     var weirdo = 1
//     if(othanumba1===0)    {
//         return weirdo
//     }
//     if(othanumba1!=1)    {
//         weirdo = exp(numba1, othanumba1-1)
//     }
//     return weirdo * numba1
// }

// console.log(exp(5,3))
// console.log(exp(2,4))
// console.log(exp(5,1))
// console.log(exp(6,0))

// function factorial(someNumba)   {
//     var maMan = 1
//     for(i=someNumba;i!==1 && i!==0;--i)  {
//         maMan *= i
//     }
//     return maMan
// }

// console.log(factorial(5)); // => 120
// console.log(factorial(4)); // => 24
// console.log(factorial(0)); // => 1

// function fibs(theVeryMehNumber) {
//   var fibNumber1 = 0;
//   var fibNumber2 = 1;
//   var variator = true;
//   var start = true;
//   var fibArray = [0];
//   for (i = theVeryMehNumber; i !== 1; i--) {
//     if (variator) {
//       fibArray.push(fibNumber2);
//       fibNumber1 += fibNumber2;
//       variator = !variator;
//     } else {
//       fibArray.push(fibNumber1);
//       fibNumber2 += fibNumber1;
//       variator = !variator;
//     }
//   }
//   return fibArray;
// }
// console.log(fibs(3)); // => [0, 1, 1]
// console.log(fibs(7)); // => [0, 1, 1, 2, 3, 5, 8]
// console.log(fibs(1));

function splitTheBill(maSquadYo) {
  maSquad = maSquadYo;
  var size = 0;
  var theFortuneWasted = 0;
  for (var key in maSquad) {
    size++;
    theFortuneWasted += maSquad[key];
  }
  for (var key in maSquad) {
    maSquad[key] -= theFortuneWasted / size;
    maSquad[key] = -maSquad[key];
  }
  return maSquad;
}

// function LoopThroughProperties(obj)
// {
//     for (var propName in obj)
//     {
//         console.log(propName + ": " + obj[propName]);
//     }
// }
var group = {
  Amy: 20,
  Bill: 15,
  Chris: 10
};

function zeroSum(array) {
  endArray = [];
  for (i = 0; i <= array.length; i++) {
    for (j = 0; j <= array.length; j++) {
      if (array[i] === -array[j])   {
          console.log(endArray)
        if (endArray.indexOf([j, i]) === -1) {
            console.log([j, i])
            endArray.push([i, j]);
        }
      }
    }
  }
  return endArray;
}

console.log(zeroSum([1, 5, 0, -5, 3, -1])); // => [[0, 5], [1, 3]]
console.log(zeroSum([1, -1])); // => [[0, 1]]
console.log(zeroSum([0, 4, 3, 5])); // => []
