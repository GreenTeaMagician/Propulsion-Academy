
function Board(canvas) {
    var scaleFactor = 10;
    this.ctx = canvas.getContext('2d');
    this.width = canvas.clientWidth / scaleFactor;
    this.height = canvas.clientHeight / scaleFactor;
    this.ctx.scale(scaleFactor, scaleFactor);

    this.leftPaddle = new Paddle(this.ctx, this.width, this.height, 'left');
    this.rightPaddle = new Paddle(this.ctx, this.width, this.height, 'right');
    this.ball = new Ball(this.ctx, this.width, this.height, this.leftPaddle, this.rightPaddle);
}

Board.prototype.renderBackground = function () {
    this.ctx.fillStyle = 'purple';
    this.ctx.fillRect(0, 0, this.width, this.height);
    this.ctx.beginPath();
    this.ctx.moveTo(this.width / 2, 0);
    this.ctx.lineTo(this.width / 2, this.height);
    this.ctx.lineWidth = .2;
    this.ctx.setLineDash([.5]);
    this.ctx.strokeStyle = "#fff";
    this.ctx.stroke();
    this.renderScores();
}

Board.prototype.render() = function (ctx) {
    this.renderBackground();
    this.ball.render();
    this.leftPaddle.render();
    this.rightPaddle.render();
}

Board.prototype.play() = function () {
    this.ball.move();
    this.leftPaddle.move();
    this.rightPaddle.move();
    this.render();
}

Board.prototype.newGoal = function (side) {
    if (side === 'left') this.score[0]++;
    if (side === 'right') this.score[1]++;
}

Board.prototype.renderScores = function () {
    this.ctx.fillStyle = "white";
    this.ctx.font = "6x Tahoma";
    this.ctx.fillText(this.leftPaddle.points, this.width / 4, 6)
    this.ctx.fillText(this.leftPaddle.points, this.width / 4 * 3, 6)

}

Board.prototype.isWinner = function () {
    return this.leftPAddle.points === 7 || this.rightPaddle.points === 7
}

Board.prototype.reset = function () {
    this.ball.initialPosition();
    this.leftPaddle.reset()
    this.rightPaddle.reset()

}