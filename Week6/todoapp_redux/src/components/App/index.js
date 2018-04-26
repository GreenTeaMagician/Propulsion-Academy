

import React, { Component } from 'react';

import Filter from '../Filter';
import Header from '../Header';
import NewTodo from '../NewToDo';
import TodoList from '../TodoList';
import { connect } from 'react-redux';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      filter: 'all',
      todos: [
        { id: 1, content: 'Learn JS', completed: true },
        { id: 2, content: 'Learn React', completed: false }
      ]
    };
  }

  addTodo = (content) => {
    const todo = {
      content,
      completed: false,
      id: this.state.todos.length + 2
    }
    const todos = this.state.todos.concat(todo);
    this.setState({ todos });
  }

  handleFilterChange = (filter) => {
    this.setState({ filter });
  }

  handleToggleCompleted = (todoId) => {
    const todo = this.state.todos.find( todo => todo.id === todoId);
    const newTodo = { ...todo, ...{ completed: !todo.completed } };
    const todos = this.state.todos.filter( todo => todo.id !== todoId);
    todos.push(newTodo);
    this.setState({ todos });
  }

  filteredTodos() {
    return this.state.todos.filter(todo => {
      if (this.state.filter === 'all') {
        return true;
      }
      if (this.state.filter === 'completed') {
        return todo.completed;
      }
      return !todo.completed;
    });
  }

  removeTodo = (todoId) => {
    const todos = this.state.todos.filter(todo => todo.id !== todoId);
    this.setState({ todos });
  }

  render() {
    return (
      <div>
        <Header />
        <NewTodo addTodo={ this.addTodo } />
        <Filter selectedFilter={ this.state.filter } onFilterChange={ this.handleFilterChange } />
        <TodoList
          onToggleCompleted={ this.handleToggleCompleted }
          onRemoveTodo={ this.removeTodo }
          todos={ this.filteredTodos() } />
      </div>
    );
  }
}

export default connect()(App);
