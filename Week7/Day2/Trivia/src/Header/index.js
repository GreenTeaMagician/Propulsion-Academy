import React, { Component } from 'react';
import logo from '../logo.svg';
import '../App.css';
import { connect } from 'react-redux';
// import store from '../store'
import Question from "../Question"


class Header extends Component {
    render() {
        return (
            <div>
            <header className='App'>
            <h2>{ this.props.title }</h2>
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                   
                    <h1 className="App-title">Welcome to React</h1>
                </header>
                <div className="App">
                    <p className="App-intro">
                        To get started, edit <code>src/App.js</code> and save to reload.
            </p>
            <p className="App-intro">Wrong answer, buddy. I have already started...</p>
                </div>
            </header>
            <Question/>
            </div>
        );
    }
}

export default connect()(Header);
