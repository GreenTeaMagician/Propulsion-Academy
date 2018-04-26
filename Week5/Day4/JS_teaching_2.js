// function add(num1, num2)    {
//     return num1 + num2 * Math.random()
// }


// function calculateNewValue(num1, num2)  {
//     arr.push(addition);
// }


// const arr = [1,2,3].map(item => item * 2)
// // const arr = [1,2,3].map(item => {
// //     return item * 2
// // });

// function fn()   {
//     console.log(this.a)
// }
// // console.log(this.a);

// function log()   {
//     console.log(b)
// }

// function a()    {
//     var b = 2;

//     return function()   {
//         console.log(b)
//     }
// }

// const arrowFn = () => {
//     console.log(this.a)
// }


// const obj =  {
//     a: 1,
//     b: 2, 
//     fn,
//     arrowFn
// };


// obj.fn();
// obj.arrowFn();

// class Car {

// }

var obj = {
    name: 'Markov'
}


console.log('-------------EXERCISE 1-------------')
function printName() {
    console.log('Thy name is: ' + this.name);
}

function myBind(theFunction, theObj) {
    return function () {
        theFunction.call(theObj)
    }
}

var boundPrint = myBind(printName, obj);
printName();
boundPrint()


console.log('-------------EXERCISE 2-------------')

var obj = {
    name: 'Markov'
}
//
function greetingsTo(name) {
    console.log('Hello ' + name + ', my name is: ' + this.name);
}
function myBind(fn, ctx) {
    const a = [].slice.call(arguments, 2)
    return function () {
        const b = [].slice.call(arguments)
        const c = a.concat(b)
        fn.call(ctx, c);
    }
};

greetingsTo('Fante');
var boundGreeting = myBind(greetingsTo, obj);
boundGreeting('Fante');

console.log('-----------EXERCISE 3-------------')

function greetingsToAll(name, name2) {
    console.log('Hello ' + name + ' and ' + name2 + ', my name is: ' + this.name);
}

function myBind(fn, ...ctxs) {
    return function (...args) {
        fn.call(...ctxs, ...args)
    }
};

greetingsToAll('Fante', 'Hornby');
var boundToAll = myBind(greetingsToAll, obj);
boundToAll('Fante', 'Hornby');

var boundAndFirst = myBind(greetingsToAll, obj, 'Fante');
boundAndFirst('Hornby');

console.log('------------EXERCISE 4 (CURRYING CALCULATOR)---------------')

// var createMultiplier = function(...args) {
//     var arr = args
//     if(arr.length===5)  {return num1 + num2 + num3 + num4 + num5}
//     else {return function(...args) {
//         var arr =+ args
//         if(arr.length===5)  {return arr[0] + arr[1] + arr[2] + arr[3] + arr[4]}
//     }}
// }

// var multiplyByFive = createMultiplier(5, 4);
// console.log(multiplyByFive)
// var nextLevelShit = multiplyByFive(4, 2);

// var multiplyByFive2 = multiplyByFive(5);
// var multiplyByFive3 = multiplyByFive2(5);
// var multiplyByFive4 = multiplyByFive3(5);

// console.log(multiplyByFive4(4)); // 20;

// var createCurryCalc = function(num1) {

// }


// var curryCalc = createCurryCalc();
// var partial1 = curryCalc(4);
// var partial2 = curryCalc(4);
// var partial3 = curryCalc(4);
// var partial4 = curryCalc(4);
// var partial5 = curryCalc(4);
// console.log(partial5());

// var curryCalc2 = createCurryCalc();
// var partial2 = curryCalc2(2);
// partial2 = partial2(4, 5)
// console.log(partial2(1, 3));

let createCalc = (n1, n2, n3, n4, n5) => n1 + n2 + n3 + n4 + n5

function currier(fn) {
    let args = [];
    const arity = fn.length;

    const curry = function () {
        const newArgs = arguments;
        args.push.apply(args, newArgs);
        if (args.length >= arity) {
            return fn.apply(null, args);
        } else {
            return curry;
        }
    };
    return curry;
}

const curriedCalc = currier(createCalc);
console.log(curriedCalc(1, 2, 3)(4, 5, 6))

console.log('------------EXERCISE 5---------------')

console.log('NOTE: The answer to this problem has already been given in Exercise 4. It is reprinted for completion.')

function currier(fn) {
    let args = [];
    const arity = fn.length;

    const curry = function () {
        const newArgs = arguments;
        args.push.apply(args, newArgs);
        if (args.length >= arity) {
            return fn.apply(null, args);
        } else {
            return curry;
        }
    };
    return curry;
}

console.log('------------EXERCISE 6---------------')

function myEach(arr, someFunc) {
    let arrEnd = []
    for(i=0;i<=arr.length-1;i++)    {
        arrEnd.push(someFunc(arr[i]))
    }
    return arrEnd
}
mySuperDuperArray = [1,2,3,4,5,6,7,8,9]
function uazgrfia(num)  {
    return num + 1000
}

console.log(myEach(mySuperDuperArray, uazgrfia))

console.log('------------EXERCISE 7---------------')

Array.prototype.map = function(someFunc) {
    return myEach(this, someFunc)
}

function cube(n)    {
    return n * n * n
}
ar = [1,2,3,4,5,6,7,8,9]

console.log(ar.map(cube))