import React, { Component } from 'react';
import { login } from "../../store/actions/index"
import { connect } from "react-redux"
import store from '../../store/index.js'
import { fetchFeed } from "../../store/actions/index"
import RaisedButton from 'material-ui/RaisedButton';
import {Tabs, Tab} from 'material-ui/Tabs';
import { Link } from 'react-router-dom';

class User extends Component {

    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <div>
            <Link to="/">Home</Link><t>   </t>
            <Link to="/feed">feed</Link><t>   </t>
            <Link to="/users">Users</Link><t>   </t>
            <Link to="/users/:userId">Specific User</Link><t>   </t>
            <Link to="/likes">Likes</Link><t>   </t>
            <div>Thats you. You are the User. </div>
        </div>
        );
    }
}

export default connect()(User)
