// import React, { Component } from 'react';
// import "./index.css"

// class NewToDo extends Component {

//     constructor(props) {
//         super(props); // remember we are inheriting from Component. We still want to call the parent initializer
//         this.state = {
//             inputText: ''
//         }; 
//     }

//     handleChange = (e) => {
//         this.setState({inputText: e.currentTarget.value})
//     }

//     handleAddTodo = () => {
//         this.props.addToDo(this.state.inputText);
//         this.setState({ inputText: '' });
//         console.log(this)
//         console.log('the thing above is this in newtodo')
//         console.log('the thing below is this this.props in newtodo')
//         console.log(this.props)
//       }


//     render() {
//         return (
//             <div>
//                 <input
//                     type="text"
//                     value={this.state.inputText}
//                     onChange={this.handleChange}
//                 />
//                 <button
//                     onClick={this.handleAddTodo}
//                 > New Todo </button>
//             </div>
//         )
//     }
// };


// export default NewToDo;


// BELOW IS THE SOLUTION
import React, { Component } from 'react';
import './index.css';
import PropTypes from 'prop-types';

class NewToDo extends Component {

    constructor(props) {
        super(props);

        this.state = {
            newTodo: ''
        }
    }

    handleAddTodo = () => {
        this.props.addTodo(this.state.newTodo);
        this.setState({ newTodo: '' });
    }

    handleNewTodoChange = (e) => {
        const newTodo = e.currentTarget.value;
        this.setState({ newTodo });
    }

    render() {
        return (
            <div className="NewTodo">
                <input
                    type="text"
                    placeholder="Add todo..."
                    value={this.state.newTodo}
                    onChange={this.handleNewTodoChange}
                />
                <button onClick={this.handleAddTodo}>Add Todo</button>
            </div>
        )
    }
}

NewToDo.propTypes = {
    addTodo: PropTypes.func.isRequired,
};

export default NewToDo;
