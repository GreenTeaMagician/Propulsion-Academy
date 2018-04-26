// import React, {Component} from 'react';
// class Header extends Component {
//     render()    {
//         return (
//             <div>
//                 <h2>{ this.props.title }</h2>
//             </div>
//         );
//     }
// }

// export default Header;

// BELOW ARE THE SOLUTIONS

import React, { Component } from 'react';
import './index.css';

class Header extends Component {

  constructor(props) {
    super(props);

    this.state = {
      quote: 'Fetching...'
    }
  }

  updateQuote() {
    fetch('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
      .then(res => res.json())
      .then(quotes => {
        this.setState({ quote: quotes[0] });
      });
  }

  componentDidMount() {
    this.updateQuote();
  }

  handleQuoteChange = () => {
    this.setState({ quote: 'Fetching...' }, () => {
      this.updateQuote();
    });
  }

  render() {
    return (
      <div className="Header">
        <h2>{ this.state.quote }</h2>
        <button className="Header-button" onClick={ this.handleQuoteChange }>
          Give me more
        </button>
      </div>
    )
  }
}

export default Header;
