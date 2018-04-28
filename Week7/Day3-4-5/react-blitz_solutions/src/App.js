import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Home from './routes/Home';
import Feed from './routes/Feed';
import Layout from './containers/Layout';
import User from './routes/User';
import Users from './routes/Users';
import store from './store';
import { fetchLocalUser } from './store/actions/currentUser';

store.dispatch(fetchLocalUser());

class App extends Component {
  render() {
    return (
      <Provider store={ store }>
        <MuiThemeProvider>
          <Router>
            <Switch>
              <Layout>
                <Route exact path="/" component={ Home } />
                <Route exact path="/feed" component={ Feed } />
                <Route exact path="/users" component={ Users } />
                <Route exact path="/users/:userId" component={ User } />
              </Layout>
            </Switch>
          </Router>
        </MuiThemeProvider>
      </Provider>
    );
  }
}

export default App;
