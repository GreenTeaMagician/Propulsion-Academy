'use strict';

function Ball(ctx, boardWidth, boardHeight, leftPaddle, rightPaddle) {
    this.ctx = ctx;
    this.width = boardWidth;
    this.height = boardHeight;
    this.position = [this.width / 2, this.height / 2];
    this.radius = 1;
    this.velocity = [1, 1];
    this.leftPaddle = leftPaddle;
    this.rightPaddle = rightPaddle;
}

Ball.prototype.render = function () {
    this.ctx.beginPath();
    this.ctx.arc(this.position[0], this.position[1], this.radius, 0, 2 * Math.PI, false);
    this.ctx.fillStyle = '#f00';
    this.ctx.fill();
}

Ball.prototype.initialPosition = function () {
    this.position = [this.width / 2, this.height / 2];
}

Ball.prototype.move = function () {
    if (this.onTopOrBottomWall()) this.velocity[1] = -this.velocity[1];
    if (this.onSideWalls()) this.velocity[0] = -this.velocity[0];
    if (this.onPaddleLeft()) this.velocity[0] = -this.velocity[0];
    if (this.onPaddleRight()) this.velocity[0] = -this.velocity[0];

    this.position[0] += this.velocity[0];
    this.position[1] += this.velocity[1];
}

Ball.prototype.onTopOrBottomWall = function () {
    return this.position[1] === this.radius
        || this.position[1] === this.height - this.radius;
}

Ball.prototype.onSideWalls = function () {
    if (this.position[0] === this.radius) {
        this.rightPaddle.points++;
        this.lightCanvas('right');
        return true;
    } else if (this.position[0] === this.width - this.radius) {
        this.leftPaddle.points++;
        this.lightCanvas('left');
        return true;
    }
}

Ball.prototype.onPaddleLeft = function () {
    var onVerticalRange =
        this.position[1] - this.radius < this.leftPaddle.position[1] + this.leftPaddle.height
        && this.position[1] + this.radius > this.leftPaddle.position[1];
    var onHorizontalRange =
        this.position[0] - this.radius === this.leftPaddle.position[0] + this.leftPaddle.width;

    return onVerticalRange && onHorizontalRange && this.velocity[0] < 0;
}


Ball.prototype.onPaddleRight = function () {
    var onVerticalRange =
      this.position[1] - this.radius < this.rightPaddle.position[1] + this.rightPaddle.height
      && this.position[1] + this.radius > this.rightPaddle.position[1];
    var onHorizontalRange =
      this.position[0] + this.radius === this.rightPaddle.position[0];
  
    return onVerticalRange && onHorizontalRange && this.velocity[0] > 0;
  }
  
  Ball.prototype.checkCollisions = function (width, height, goalFunction) {
    if (this.pos[0] - radius === 0 || this.pos[0] + radius === width) {
      const side = this.pos[0] - radius === 0 ? 'left' : 'right';
      this.vel[0] = -this.vel[0];
      goalFunction(side)
    }
  
    if (this.pos[1] - radius === 0 || this.pos[1] + radius === height)
      this.vel[1] = -this.vel[1];
  }
  
  
  Ball.prototype.lightCanvas = function(side) {
    var that = this;
    var lightIt = function() {
      that.ctx.fillStyle = '#f00';
      side === 'left'
        ? that.ctx.fillRect(0, 0, that.width / 2, that.height)
        : that.ctx.fillRect(that.width / 2, 0, that.width, that.height);
    };
    
    lightIt();
    var interval  = setInterval(lightIt, 25);
    setTimeout(clearInterval.bind(null, interval), 100);
  }