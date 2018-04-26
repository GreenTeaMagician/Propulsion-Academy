

function game() {

}

class Ball {
    constructor(xpos, ypos, radius) {
        this.radius = radius
        this.ypos = ypos;
        this.xpos = xpos;
        this.fillStyle = '#000000';
        this.xVel = 2
        this.yVel = 2
    }

    updatePos() {
        if ((ball.xpos === paddle1.xpos || ball.xpos === paddle2.xpos) && ((ball.ypos <= paddle1.ypos + paddle1.height && ball.ypos >= paddle1.ypos) || (ball.ypos <= paddle2.ypos + paddle2.height && ball.ypos >= paddle2.ypos))) {
            ball.xVel = -ball.xVel
        }
        if (ball.ypos === 666 || ball.ypos === 0) {
            ball.yVel = -ball.yVel
        }
        ball.xpos += ball.xVel
        ball.ypos += ball.yVel
    }
    render(context) {
        context.beginPath();
        context.arc(this.width, this.height, this.radius, 0, 2 * Math.PI);
        context.stroke();
        context.fillStyle = 'white';
        context.fill();
    }
}

class Paddle {
    constructor(width, height, xpos, ypos) {
        this.width = width;
        this.height = height;
        this.xpos = xpos;
        this.ypos = ypos;
        this.white = 'white'
    }
    updatePaddle() {

    }
    render(context) {
        context.fillStyle = "#FFFFFF";
        context.fillRect(this.width, this.height, this.xpos, this.ypos);
    }
}


// var ball = new Ball(400, 400, 5);

// ctxBall.beginPath();
// ctxBall.arc(ball.width, ball.height, ball.radius, 0, 2 * Math.PI);
// ctxBall.stroke();
// ctxBall.fillStyle = 'white';
// ctxBall.fill();

function Game() {

    this.paddle1 = new Paddle(860, 150, 10, 100)
    this.paddle2 = new Paddle(40, 300, 10, 100)

    this.ball = new Ball(400, 400, 5);

    console.log('This is the end of Game()')

    // var hereWeGoooooo = setInterval(game(), 200)
}

function renderLine(gameCanvas) {
    
    gameCanvas.fillStyle = 'black';
    gameCanvas.fillRect(10, 10, 1000, 666);
    
    gameCanvas.setLineDash([11, 5]);/*dashes are 5px and spaces are 3px*/
    gameCanvas.beginPath();
    gameCanvas.moveTo(450, 0);
    gameCanvas.lineTo(450, 900);
    gameCanvas.strokeStyle = '#FFFFFF';
    gameCanvas.stroke();
}

Game.prototype.run = function () {
    this.canvas = document.getElementById   ('myCanvas');
    this.gameCanvas = this.canvas.getContext('2d');

    renderLine(this.gameCanvas)
    
    this.paddle1.render(this.gameCanvas)
    this.paddle2.render(this.gameCanvas)
    // this.gameCanvas.fillRect(860, 150, 10, 100);

    this.gameCanvas.beginPath();
    this.gameCanvas.arc(this.ball.width, this.ball.height, this.ball.radius, 0, 2 * Math.PI);
    this.gameCanvas.stroke();
    this.gameCanvas.fillStyle = 'white';
    this.gameCanvas.fill();


    console.log('End of run()')
}

var game = new Game();
game.run()