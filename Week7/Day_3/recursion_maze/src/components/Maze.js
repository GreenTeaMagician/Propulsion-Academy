import React, { Component } from 'react';

export class Maze extends Component {

    render() {
        let rows = []
        let row = 0;
        let col = 0;

        if (this.props.maze) {
            for(let r of this.props.maze) {
                let cells = []
                for( let c of r) {
                    let cellID = `cell${row}-${col}`
                    let classes = [];
                    if (c.left) classes.push("left");
                    if (c.right) classes.push("right");
                    if (c.top) classes.push("top");
                    if (c.bottom) classes.push("bottom");
                    if (c.end) classes.push("end");
                    if (c.onpath) classes.push("onpath");
                    if (c.visited) classes.push("visited");



                    cells.push(<td key={cellID} id={cellID} className={classes.join(" ")}>&nbsp;</td>);
                    col++;
                }
                rows.push(<tr key={row} >{cells}</tr>);
                row++;
            }
        }

        return (
            <table id="simple-board">
            <tbody>
              {rows}
             </tbody>
             </table>
        )
    }

}