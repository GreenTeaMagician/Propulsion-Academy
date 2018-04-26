import React, { Component } from 'react';
import './App.css';
import Header from './Header'
import { connect } from 'react-redux';
import addQuestion from './actions';
import Question from './Question'


class App extends Component {

  componentDidMount() {
    for(var i=0;i<=9;i++)  {
    fetch('https://opentdb.com/api.php?amount=1')
      .then(response => response.json())
      .then(data => {
        const action = addQuestion(data);
        this.props.dispatch(action);
        console.log('In the fetch. Ahh, general Kenobi!')
        console.log(action)
        })
      }
  }

  componentArray = [<Header />, <Question />,]

  render() {
    return (
      <div>
        
      <Header />
      </div>
    );
  }
}

export default connect()(App);
