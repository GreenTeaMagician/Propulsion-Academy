import React from 'react';
import ReactDOM from 'react-dom';
import store from "./store/index"
import { Provider } from "react-redux"
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import registerServiceWorker from './registerServiceWorker';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Likes from './Components/Likes'
import Login from './Components/Login'
import Feed from './Components/Feed'
import Users from './Components/Users'
import User from './Components/User'

ReactDOM.render(
    <Provider store={store}>
        <MuiThemeProvider>
        <Router>
      <Switch>
        <Route exact path="/" component={ Login } />
        <Route exact path="/feed" component={ Feed } />
        <Route exact path="/users" component={ Users } />
        <Route exact path="/users/:userId" component={ User } />
        <Route exact path="/likes" component={ Likes } />
        </Switch>
        </Router>
        </MuiThemeProvider>
    </Provider>,
    document.getElementById('root'));
registerServiceWorker();
