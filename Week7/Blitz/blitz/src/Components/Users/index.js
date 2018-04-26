import React, { Component } from 'react';
import { connect } from "react-redux"
import { Link } from 'react-router-dom';

class Users extends Component {

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

            <div>Nope, nothing to see here, go please move on, Ladies and gentlemen</div>
            </div>
        );
    }
}

export default connect()(Users)
