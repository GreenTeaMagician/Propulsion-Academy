import React, { Component } from 'react';
// import { connect } from 'react-redux';
import index from '../../index.css'
import { login } from "../../store/actions/index"
import { connect } from "react-redux"
import { Link } from 'react-router-dom';


class Login extends Component {

    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '',
            token: '',
            LogResponse: ''
        };
    }


    handleUsername = (event) => {
        this.setState({
            email: event.target.value,
        });
    }

    handlePassword = (event) => {
        this.setState({
            password: event.target.value
        });
    }

    logout = (e) => {
        e.preventDefault()
        console.log('Logging out...')
        localStorage.clear()
        window.location.reload();
    }

    submitForm = (e) => {
        e.preventDefault()
        console.log(localStorage.getItem('token'))
        console.log(this.state)
        this.props.dispatch(login(this.state))
        console.log(this)
    }

    render() {
        return (
                    <div className='top-container'>
                        <div className="App-intro">
            <Link to="/">Home</Link><t>   </t>
            <Link to="/feed">feed</Link><t>   </t>
            <Link to="/users">Users</Link><t>   </t>
            <Link to="/users/:userId">Specific User</Link><t>   </t>
            <Link to="/likes">Likes</Link><t>   </t>
                            <div className='centerStuff'>
                                <form onSubmit={this.submitForm}>
                                    <div className='IntroT'>
                                        Username: <br />
                                        <input type="text" onChange={this.handleUsername} value={this.state.email}></input>
                                    </div>
                                    <div>
                                        Password: <br />
                                        <input type="password" onChange={this.handlePassword} value={this.state.password}></input>
                                    </div>
                                    <button className='loginbutton' onClick={this.submitForm}>Login</button>
                                    <button className='logoutbutton' onClick={this.logout}>Logout</button>
                                </form>
                                <div>{this.state.LogResponse}</div>
                            </div>
                        </div>
                    </div>
        );
    }
}

export default connect()(Login)