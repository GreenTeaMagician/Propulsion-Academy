import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './components/App';
import Intro from './components/Intro';
import GBAngular from './components/App';
import TodoList from './components/App';
import registerServiceWorker from './registerServiceWorker';
import { Provider } from 'react-redux';

ReactDOM.render(
    <Provider>
    <App />
    </Provider>,
    document.getElementById('root'));

console.log('Hello cruel world')

// BELOW IS THE THE SOLUTION

// import React from 'react';
// import ReactDOM from 'react-dom';
// import App from './App';
// import './index.css';

// ReactDOM.render(
//   <App />,
//   document.getElementById('root')
// );
