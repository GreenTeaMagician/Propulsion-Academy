import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

//...

ReactDOM.render(
  <Provider store={ store }>
    <Router>
      <Switch>
        <Route exact path="/" component={ Home } />
        <Route exact path="/question/:order" component={ Feed } />
        <Route exact path="/result" component={ Users } />
      </Switch>
    </Router>
  </Provider>,
  document.getElementById('root')
);

