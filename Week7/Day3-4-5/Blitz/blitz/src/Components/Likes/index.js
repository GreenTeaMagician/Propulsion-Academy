import React, { Component } from 'react';
import { connect } from "react-redux"
import { Link } from 'react-router-dom';
import { fetchLikes } from "../../store/actions/index"

class Likes extends Component {

    constructor(props) {
        super(props);
        this.state = {

        };
    }

    fetchLikes = (e) => {
        e.preventDefault()
        this.props.dispatch(fetchLikes())
    }

    render() {
        console.log("the props from the state", this.props.state)
        return (<div>
            <Link to="/">Home</Link><t>   </t>
            <Link to="/feed">feed</Link><t>   </t>
            <Link to="/users">Users</Link><t>   </t>
            <Link to="/users/:userId">Specific User</Link><t>   </t>
            <Link to="/likes">Likes</Link><t>   </t>
            <div>No ones likes you. Go away.</div>
            <button type='button' onClick={this.fetchLikes}>Fetch Likes</button>
            hello there!
            {
                this.props.likes.map(t =>
                    <span key={t._id} id={t._id}>
                        {t.content}
                        <t> by </t>{t._user.username}
                    </span>
                )
            }
        </div>
        );
    }
}
const mapStateToProps = (state) => {
    return {
        likes: state.likeReducer
    }
}
export default connect(mapStateToProps)(Likes)
