import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
        <Router>
        <Switch>
          <Route exact path="/" component={ Home } />
          <Route exact path="/question/:order" component={ Feed } />
          <Route exact path="/result" component={ Users } />
        </Switch>
      </Router>
    );
  }
}

export default App;