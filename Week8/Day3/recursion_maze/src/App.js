import React, { Component } from 'react';
import {Maze} from './components/Maze'
import './App.css';
import * as gm from 'generate-maze'
import {mazeSolver} from './MazeSolver'

function removeWalls(maze, r, c) {
  maze[r][c].left = maze[r][c -1].right = false;
  maze[r][c].top = maze[r - 1][c].bottom = false;
  maze[r][c].right = maze[r][c+1].left = false;
  maze[r][c].bottom = maze[r+1][c].top = false;
}
function newMaze() {
  let size = 120
  let maze = gm(size)
  // make bit mor tricky with possible loops
  removeWalls(maze, Math.floor(size/2), Math.floor(size/2) );

  maze[size -1][ size - 1].end = true;
  maze[0][0].onpath = true;
  return maze;
}

let maze =  newMaze();

class App extends Component {


  render() {
    return (
      <div className="App">
        <button href="#" onClick={ () => { mazeSolver(maze, 0,0); this.forceUpdate(); }}  >Solve </button>
        or
        <button href="#" onClick={ () => { maze = newMaze(); this.forceUpdate(); }}  > New Maze </button>
        <Maze maze={maze}/>
      </div>
    );
  }
}

export default App;
