const INCR = 'increment';
const DECR = 'decrement'

const counterReducer = (state = 0, action) => {
  switch (action.type) {
    case INCR:
      return state + 1;
    case DECR:
      return state - 1;
    default:
      return state;
  }
}

const ADD_TODO = 'addTodo';

const initialTodos = ['Learn Redux', 'Learn React Redux', 'Master React'];

const todosReducer = (state = initialTodos, action) => {
  switch (action.type) {
    case ADD_TODO:
      return state.concat([action.data]);
    default:
      return state;
  }
}

const reducer = Redux.combineReducers({
  counter: counterReducer,
  todos: todosReducer,
});

const store = Redux.createStore(reducer);
store.subscribe(render);

function render() {
  const counterEl = document.getElementById('counter');
  const state = store.getState();
  counterEl.innerHTML = state.counter;
  const todosList = document.getElementById('todos');
  todosList.innerHTML = '';
  for (var i = 0; i < state.todos.length; i++) {
    const todoEl = document.createElement('li');
    todoEl.innerHTML = state.todos[i];
    todosList.appendChild(todoEl);
  }
}

document
  .getElementById('increment')
  .addEventListener('click', function() {
    store.dispatch({ type: INCR });
  });

document
  .getElementById('decrement')
  .addEventListener('click', function() {
    store.dispatch({ type: DECR });
  });

document
  .getElementById('add-todo')
  .addEventListener('click', function() {
    const newTodo = document.getElementById('new-todo').value;
    store.dispatch({
      type: ADD_TODO,
      data: newTodo,
    });

    document.getElementById('new-todo').value = '';
  })

render();
