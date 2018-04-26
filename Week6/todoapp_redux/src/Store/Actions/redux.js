
let store = Redux.createStore(reducer)

const iniState = { state: "Hello World" }

todos: [
    { id: 1, content: 'Learn JS', completed: true },
    { id: 2, content: 'Learn React', completed: false }
  ]

  reducer = (state = initialState, action) => {
    switch (action.type) {
        case "NewToDo": {
            const newState = { ...state };
            newState.counter++
            return newState
        }
        default:
            return state
    }
}; 