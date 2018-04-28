

function Paddle(ctx, boardWidth, boardHeight, side) {
    this.ctx = ctx;
    this.boardWidth = boardWidth
    this.boardHeight = boardHeight
    this.width = 1;
    this.height = 15;
    this.position = []
    this.side = side
    this.direction = [0, 0]
    this.points = 0;
    this.setPosition()
    this.setListeners()
}

Paddle.prototype.setPosition = function () {
    this.position[1] = this.boardHeight / 2 - this.height / 2
    this.position[0] = this.side == 'left' ? 2 : this.boardWidth - this.width - 2 //what the fuck is this
}

Paddle.prototype.render = function () {
    this.ctx.fillStyle = 'white';
    this.ctx.fillRect(this.position[0], this.position[1], this.width, this.height)
}

Paddle.prototype.move = function () {
    this.position[1] += this.direction[1];
    if (this.position[1] < 0) {
        this.position[1] = 0;
    }
    else if (this.position[1] + this.height > this.boardHeight) {
        this.position[1] = this.boardHeight - this.height;
    }
}

Paddle.prototype.setListeners = function () {
    document.addEventListener('keydown', function (e) {
        var speed = 1;
        var key = e.key
        if (this.side === 'left') {
            if (key === 'w') this.direction[1] = -speed;
            if (key === 's') this.direction[1] = speed;
        } else if (this.side === 'left') {
            if (key === 'ArrowUp') this.direction[1] = -speed;
            if (key === 'ArrowDown') this.direction[1] = speed;
        }
    }.bind(this))

    document.addEventListener('keyup', function (e) {
        var key = e.key;
        if(this.side === 'left' && (key === 'w' || key=== 's')) this.direction[1] = 0;
        if(this.side === 'left' && (key === 'ArrowUp' || key=== 'ArrowDown')) this.direction[1] = 0;
    });

    Paddle.prototype.reset = function () {
        this.points = 0;
        this.setPosition();
    }
}