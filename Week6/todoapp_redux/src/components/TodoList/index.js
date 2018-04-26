import React, { Component } from 'react';

import TodoListItem from '../TodoItem';
import './index.css';
import PropTypes from 'prop-types';

class TodoList extends Component {

  render() {
    return (
      <div className="TodoList">
        <ul>
          {
            this.props.todos.map((todo, index) =>
              <TodoListItem
                key={ todo.id }
                todo={ todo }
                onRemoveTodo={ this.props.onRemoveTodo }
                onToggleCompleted={ this.props.onToggleCompleted }
              />
            )
          }
        </ul>
      </div>
    );
  }
}

TodoList.propTypes = {
  onToggleCompleted: PropTypes.func.isRequired,
  onRemoveTodo: PropTypes.func.isRequired,
  todos: PropTypes.array
}

export default TodoList
