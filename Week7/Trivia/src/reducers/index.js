import { combineReducers } from 'redux';
// import { connect } from 'react-redux';

// import filter from './filter';
// import todos from './todos';



const newQ_reducer = function (state = {}, action) {
    switch (action.type) {
        case "new_question":
            let newState = [...state]
            let finalState = newState.concat([action.payload])
            console.log('In newQ_reducer. Hello there!')
            return finalState
        default:
            return state
    }
}

export default combineReducers({
      newQ_reducer
    //   todos,
});