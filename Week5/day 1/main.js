console.log('Hello Neo...')

if(true)  {
  console.log("I am Morpheus")
} else if(false)  {
  console.log("daFaaaqq")
} else { 
  console.log("Miss me with that gay shit")
}

var arr = [1,2,3,4,5,6]
var string = ' shots so far'
for (var i = 0; i < arr.length; i++)  {
  console.log('I have taken ' + i + string)
  string += 'rr'
}

for(var j of arr) {
  console.log(j);
}

console.log('---forEach---')
arr.forEach(function(item) {
  console.log('item')
});

console.log('---map---')
var newArr = arr.map(function(item) {
  return item * 2
});

console.log('---while---')
var k = 4
while(k != 0) {
  k--;
}

console.log('---operators---')
console.log(1=='1');
console.log(1==='1');

function factorial(n) {
  if(n === 0 || n == 1) {
    return 1
  }
  return n * factorial(n - 1);
}

function countDown(n) {
  console.log(n)
  if(n === 0) {
    return 0;
  }
  return countDown(n--)
}

function doSth(num1, num2)  {
  console.log(num1);
  console.log(num2);
  return num1 + num2;
};

function convert(numOrderPls)   {
  var numArr = String(numOrderPls).split('')
  console.log(numArr)
  for(i=0;i<=numArr.length - 1;i++)   {
      numArr[i] = Number(numArr[i])
  }
  return numArr.sort().reverse()
}

var myNumber = 2
var MyClass //Pascal case ---> subset of CamelCase/camelCase
var MY_CONSTANT = true

