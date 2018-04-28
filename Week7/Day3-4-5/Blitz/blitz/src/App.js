import React, { Component } from 'react';
import './App.css';
import Login from './Components/Login/index.js'
import Feed from './Components/Feed'
import {Tabs, Tab} from 'material-ui/Tabs';
import Users from './Components/Users'
import User from './Components/User'


// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// import { Provider } from 'react-redux';

class App extends Component {
  render() {
    return (
      <div>
        <Tabs>
          <Tab label="Login">
            <Login />
          </Tab>
          <Tab label="Feed">
            <Feed />
          </Tab>
          <Tab label="Users">
          <Users />
          </Tab>
          </Tabs >
          <User />
      </div>
          );
        }
      }
      
      export default App;
