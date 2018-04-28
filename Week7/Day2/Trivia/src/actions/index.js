// import { connect } from 'react-redux';


var addQuestion = (data) => {
    return {
        type: 'add_question',
        payload: data
    }
}
export const ADD_TODO = 'addTodo';

export const addTodo = (content) => ({
    type: ADD_TODO,
    content,
  });

// export default connect()(addQuestion);
export default addQuestion;