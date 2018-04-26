// hello = 'hi'
// ya = 'ya'
// hello += ya

// var e = ['a', 'b']

// for(var i=0;i<=10;i++)  {
//     e.charAt(i)
// }

// a = 
// arr = [0]
// console.log(arr)
// arr.push(1)
// console.log(arr)
// endArray = ['b', 'c', [5,6]]
// console.log(endArray.indexOf([5,6]))

function Ball(width, height, radius) {
    this.radius = radius
    this.height = height;
    this.width = width;
    this.fillStyle = '#FF0000';
}

var ball = new Ball(40, 40, 40)

function testGame() {
    console.log(ball.height)
}