function doSth()    {
    const a = []
    a.push(1);
    a = [];
}
let count = 0
function count()    {
    count++;
    console.log(`Count is : ${count}`)
}

let count1 = 0
function count1()    {
    count1++;
    console.log(`Count1 is : ${count1}`)
}

console.log('-----------------------------')

function Person()   {
    this.name = name
    this.greet = function()     {
        console.log(`Hi, my name is ${this.name}`)
    }
}

Person.prototype.greet = function() {
    console.log(`Hi my name is ${this.name}`)
}

var laurent = new Person('Laurent');
laurent.greet();

function Coder(name)    {
    Person.call(this, name)
    this.skill = 'can code'
    Object.setPrototypeOf(this, Person.prototype)
}

Coder.prototype = Object.create(Person.prototype)

Coder.prototype.code = function()   {console.log('condingggg')}

var laurentCoder = new Coder('Laurent')