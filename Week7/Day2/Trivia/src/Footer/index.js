import React, { Component } from 'react';
import logo from '../logo.svg';
import '../App.css';
import { connect } from 'react-redux';


class Footer extends Component {
    render() {
        return (
            <div>
                <p>Hello there!</p>
            </div>
        );
    }
}

export default connect()(Footer);
