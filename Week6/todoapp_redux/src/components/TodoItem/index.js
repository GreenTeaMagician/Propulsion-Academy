// import React, {Component} from 'react';
// import "./index.css"
// import PropTypes from 'prop-types';

// class TodoItem extends Component {

//   // render()  {
//   //   return <li>HERRROooo</li>
//   // }

//   }

//   TodoItem.propTypes = {
//     todo: PropTypes.string
//   };

// export default TodoItem;

// BELOW IS THE SOLUTION

import React, { Component } from 'react';

import './index.css';
import PropTypes from 'prop-types';


class TodoListItem extends Component {

  handleRemoveTodo = () => {
    this.props.onRemoveTodo(this.props.todo.id);
  }

  handleToggleCompleted = () => {
    this.props.onToggleCompleted(this.props.todo.id);
  }

  render() {
    return (
      <li>
        <span
          onClick={ this.handleToggleCompleted }
          className={ this.props.todo.completed ? 'TodoListItem-completed' : '' }
        >
          { this.props.todo.content }
        </span>
        <button onClick={ this.handleRemoveTodo }>X</button>
      </li>
    )
  }
}

TodoListItem.propTypes = {
  onRemoveTodo: PropTypes.func.isRequired,
  onToggleCompleted: PropTypes.func.isRequired,
  todo: PropTypes.shape({
    content: PropTypes.string.isRequired,
    completed: PropTypes.bool.isRequired,
    id: PropTypes.number.isRequired
  }).isRequired
}

export default TodoListItem;
