import React, { Component } from 'react';
// import logo from '../logo.svg';
import '../App.css';
import { connect } from 'react-redux';
// import Header from '../Header/index.js'
import store from '../store';
import Footer from '../Footer';
import '../App.css';
import addQuestion from '../actions'

class Question extends Component {

    constructor(props) {
        super(props);

        this.state = {
            newToDo: ''
        }
    }

    onClick = () => {
        console.log('Inside button click. pls stop clicking me...')
        const action = addQuestion(this.state.newToDo)
        this.props.dispatch(action);
        this.setState({ newToDo: '' });
    }
    stateChange = (e) => {
        // console.log('Inside onChange. Charmander is evolving!')
        const newToDo = e.currentTarget.value;
        this.setState({ newToDo });
    }

    render() {
        return (
            <div>
                <div className="NewTodo">
                    {/* <input
                        type="text"
                        placeholder="Add todo..."
                        value = { this.state.newToDo }
                        onChange = { this.stateChange }
                        className="magic-Button"
                    /> */}
                    <div className='magicButton'>
                        <button onClick={this.onClick}>Give me a Question!</button>
                    </div>
                </div>
                {/* <Footer /> */}
            </div>

        );
    }
}

export default connect()(Question);













