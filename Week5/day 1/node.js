var asciify = require("asciify");

function isString(strOrNah) {
  if (typeof strOrNah !== "string") {
    return false;
  } else {
    return true;
  }
}

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

function longest(s1, s2) {
  var longString = [s1, s2].reduce(function(a, b) {
    return a.length > b.length ? a : b;
  });
  var charList = "";
  for (i = 0; i <= longString.length; i++) {
    if (charList.indexOf(s1.charAt(i)) <= -1) {
      charList += s1.charAt(i);
    }
    if (charList.indexOf(s2.charAt(i)) <= -1) {
      charList += s2.charAt(i);
    }
  }
  return charList
    .split("")
    .sort()
    .join("");
}

function convert(numOrderPls) {
  var numArr = String(numOrderPls).split("");
  console.log(numArr);
  for (i = 0; i <= numArr.length - 1; i++) {
    numArr[i] = Number(numArr[i]);
  }
  return numArr.sort().reverse();
}

function countArr(howManyDude) {
  var authors = new Object();
  for (i = 0; i <= howManyDude.length - 1; i++) {
    if (howManyDude[i] in authors) {
      authors[howManyDude[i]] += 1;
    } else {
      authors[howManyDude[i]] = 1;
    }
  }
  return authors;
}

function isCaught(tomAndJerry) {
  for (i = 0; i <= tomAndJerry.length; i++) {
    if (tomAndJerry[i] == "C") {
      tomIndex = i;
    }
    if (tomAndJerry[i] == "m") {
      jerryIndex = i;
    }
  }
  try {
    return Math.abs(jerryIndex - tomIndex) >= 4 ? false : true;
  } catch (e) {
    return "Either Tom is still asleep, or Jerry escaped. A sad day indeed...";
  }
}

function splitTheBill(maSquadYo) {
    maSquad = maSquadYo
    var size = 0
    var theFortuneWasted = 0
    for (var key in maSquad) {
        size++;
        theFortuneWasted += maSquad[key]
    }
    for(var key in maSquad)   {
        maSquad[key] -= theFortuneWasted/size
        maSquad[key] = -maSquad[key]
    }
    return maSquad
};

function exp(numba1, othanumba1) {
    var weirdo = 1
    if(othanumba1===0)    {
        return weirdo
    }
    if(othanumba1!=1)    {
        weirdo = exp(numba1, othanumba1-1)
    }
    return weirdo * numba1
}

function factorial(someNumba)   {
    var maMan = 1
    for(i=someNumba;i!==1 && i!==0;--i)  {
        maMan *= i
    }
    return maMan
}

function fibs(theVeryMehNumber) {
    var fibNumber1 = 0;
    var fibNumber2 = 1;
    var variator = true;
    var start = true;
    var fibArray = [0];
    for (i = theVeryMehNumber; i !== 1; i--) {
      if (variator) {
        fibArray.push(fibNumber2);
        fibNumber1 += fibNumber2;
        variator = !variator;
      } else {
        fibArray.push(fibNumber1);
        fibNumber2 += fibNumber1;
        variator = !variator;
      }
    }
    return fibArray;
  }

module.exports = {
  isString: isString,
  isArray: isArray,
  areSameType: areSameType,
  longest: longest,
  convert: convert,
  countArr: countArr,
  isCaught: isCaught,
  splitTheBill: splitTheBill,
  exp: exp,
  factorial: factorial,
  fibs: fibs,
};
