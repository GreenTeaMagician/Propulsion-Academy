import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from 'App.js'

import { createStore} from 'redux'


//...

ReactDOM.render(
  <Provider store={ store }>
    <App />
  </Provider>,
  document.getElementById('root')
);
