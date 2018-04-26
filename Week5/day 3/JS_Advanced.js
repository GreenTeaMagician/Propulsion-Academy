

// console.log('----------------Exercise 1----------------------')
// var myMath = Object.create(Math);

// console.log(myMath.sqrt(9))

// myMath.randomInt = function (max) {
//     return this.floor(this.random() * this.floor(max));
// };


// console.log(myMath.randomInt(5)); // 3 for example
// console.log(myMath.randomInt(10)); // 10 for example
// console.log(myMath.random()); // some random number between 0 and 1
// console.log(myMath.round(0.5));
// console.log(myMath.randomInt(10, -4));

// console.log('----------------Exercise 2----------------------')

// String.prototype.reverse = function () {
//     return this.split("").reverse().join("");
// }
// console.log('hello'.reverse());

// console.log('----------------Exercise 3----------------------')

// futureMe = { apple: 'Expert', linux: 'pretty good', family: 'yes', retirementFunds: 'millions' }
// me = { windows: 'Expert', apple: 'eh', linux: 'no', videoGames: 'ok', retirementFunds: 'lolBitchYouThinkICare' }
// kidMe = { takingTrain: 'good', buildKnex: 'The Best' }

// function merge(object1, ...args) {
//     var finalObject = Object.create(object1);
//     for (i = 0; i <= arguments.length-1; i++) {
//         finalObject = Object.assign(arguments[i], arguments[i - 1]);
//     }
//     return finalObject
// }

// var myFinalForm = merge(futureMe, me, kidMe)
// console.log(myFinalForm)
// console.log('----------------Exercise 4----------------------')

// function invert(object) {
//     var finalObject = {}
//     for (var key in object) {
//         finalObject[object[key]] = key
//     }
//     return finalObject
// }
// console.log(invert({ a: 3, b: 2 }));

console.log('----------------Exercise 5----------------------')

futureMe = { apple: 'Expert', linux: 'pretty good', family: 'yes', retirementFunds: 'millions' }

Object.prototype.keys = function () {
    this.finalArray = []
    for (var key in this) {
        this.finalArray.push(key)    
    }
    return this.finalArray.sort()
}

console.log(futureMe.keys())

console.log('----------------Exercise 6----------------------')
