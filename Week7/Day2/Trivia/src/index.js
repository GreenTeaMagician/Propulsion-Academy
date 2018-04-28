import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import { Provider } from 'react-redux';
import store from './store/index.js';
import Question from './Question'
import Footer from './Footer'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

const toZeKwesstschons = () => {
    
}

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Switch>
                <Route exact path="/" component={App} onEnter={toZeKwesstschons()}/>
                <Route exact path="/question/:order" component={Question} />
                <Route exact path="/result" component={Footer} />
            </Switch>
        </Router>
    </Provider>,
    document.getElementById('root'));
registerServiceWorker();
