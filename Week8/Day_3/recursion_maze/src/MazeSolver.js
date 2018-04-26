/* 
    Maze is 2D Array. Each Maze element (cell) looks like
    {
      x: 4,          // Horizontal position, integer
      y: 7,          // Vertical position, integer
      top: false,    // Top/Up has a wall/blocked if true, boolean 
      left: false,   // Left has a wall/blocked if true, boolean
      bottom: true,  // Bottom/Down has a wall/blocked if true, boolean
      right: true,   // Right has a wall/blocked if true, boolean
      set: 5         // Set # used to generate maze, can be ignored
    
      end: false     // true if this is the end cell you should find a path to

      // these can be set by you:
      visited: false // your algorithm visited this place already once
      onpath: false // this cell is on your solutions path to the end
    }
*/

// function that finds the end cell from the start position row, col
// returns true if it can find it, false otherwise


export function mazeSolver(maze, row, col) {
  var solved = false
  // console.log(`At ${row}, ${col}`);
  maze[row][col].onpath = true

  if (maze[row][col].end === true) {
    return true
  }

  //Going in different directions

  //Going right
  if (!solved) {
    if (maze[row][col].right === false) {
      if (maze[row][col + 1].visited === undefined) {
        maze[row][col].visited = true
        maze[row][col].onpath = false

        solved = mazeSolver(maze, row, col + 1)
      }
    }
  }

  //Going down
  if (!solved) {
    if (maze[row][col].bottom === false) {
      if (maze[row + 1][col].visited === undefined) {
        maze[row][col].visited = true
        maze[row][col].onpath = false
        solved = mazeSolver(maze, row + 1, col)
      }
    }
  }

  //Going left
  if (!solved) {
    if (maze[row][col].left === false) {
      if (maze[row][col - 1].visited === undefined) {
        maze[row][col].visited = true
        maze[row][col].onpath = false
        solved = mazeSolver(maze, row, col - 1)
      }
    }
  }


  //Going up
  if (!solved) {
    if (maze[row][col].top === false) {
      if (maze[row - 1][col].visited === undefined) {
        maze[row][col].visited = true
        maze[row][col].onpath = false
        solved = mazeSolver(maze, row - 1, col)
      }
    }
  }

  maze[row][col].onpath = false
  maze[row][col].visited = true

  if (solved) {
    maze[row][col].onpath = true
    maze[row][col].visited = false
  }
  return solved

  // //Going up
  // if (maze[row][col].bottom === false) {
  //   if (maze[row][col].visited !== false) {
  //     if (maze[row - 1][col] !== undefined) {
  //       maze[row][col].onpath = false
  //       maze[row][col].visited = true
  //       mazeSolver(maze, row - 1, col)
  //     }
  //   }
  // }



  // if(maze[row][col].bottom===false) {
  //   console.log('inside first if loop')
  //   console.log(maze[row][col].visited)

  //   if(maze[row][col].visited !== false)  {
  //     console.log('made it to here')
  //     maze[row][col].onpath = false
  //     maze[row][col].visited = true
  //     mazeSolver(maze, row, col+1)
  //   }
  // }

}