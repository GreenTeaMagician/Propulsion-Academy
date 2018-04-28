'use strict';

function Game(canvas) {
  this.canvas = canvas;  
  this.startPlayBind = this.startGame.bind(this);
  this.gameInterval;
  this.board = new Board(this.canvas);

  this.initializeGame();
}

Game.prototype.initializeGame = function() {
  window.addEventListener('keypress', this.startPlayBind); 
  this.board.render();
}

Game.prototype.startGame = function() {
  window.removeEventListener('keypress', this.startPlayBind);
  this.gameInterval = setInterval(this.play.bind(this), 16.6);
}

Game.prototype.play = function () {
  this.board.play();
  if(this.board.isWinner()) {
    clearInterval(this.gameInterval);
    this.board.reset();
    setTimeout(this.initializeGame.bind(this), 2000);
  }
}
