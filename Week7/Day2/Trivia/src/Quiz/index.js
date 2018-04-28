import React, { Component } from 'react';
import '../App.css';
import { connect } from 'react-redux';
import store from '../store';
import Footer from '../Footer';
import '../App.css';
import addQuestion from '../actions'

class Quiz extends Component {

    constructor(props) {
        super(props);

        this.state = {
            newToDo: ''
        }
    }

    render() {
        return (
            <div>
                <div>
                    Hello there!
                </div>
            </div>
        );
    }
}

export default connect()(Question);













