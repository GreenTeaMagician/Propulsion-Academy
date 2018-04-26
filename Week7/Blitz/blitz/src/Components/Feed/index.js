import React, { Component } from 'react';
import index from '../../index.css'
import { connect } from "react-redux"
import { fetchFeed } from "../../store/actions/index"
import { Link } from 'react-router-dom';
import smiley from './smiley.jpg'
import nooooooo from './noooooo.jpg'
import smiley_c from './smiley_clicked.jpg'
import nooooooo_c from './noooooo_clicked.jpg'

class Feed extends Component {

    constructor(props) {
        super(props);
        this.state = {

        };
    }
    fetchFeed = (e) => {
        e.preventDefault()
        this.props.dispatch(fetchFeed())
        console.log(this.props)
    }

    checkLike(likeStatus) {
        if (likeStatus) {
            return <img src={smiley_c}
                alt="ToTheTop"
                width='20px'
                height='20px'
                // onClick={() => this.changeSmiley()}
                >
            </img>
        } else {
            return;
        }

    }

    changeSmiley(id) {
        console.log(id)
        var pic = document.getElementById(id)
        console.log(pic)
        console.log(document.getElementById(id).src)
        if (pic !== -1) {
            document.getElementById(id).src = smiley_c;
        }
        else {
            document.getElementById(id).src = smiley;
        }
    }




    render() {
        // console.log(this.props);

        return (
            <div>
                <Link to="/">Home</Link><t>   </t>
                <Link to="/feed">feed</Link><t>   </t>
                <Link to="/users">Users</Link><t>   </t>
                <Link to="/users/:userId">Specific User</Link><t>   </t>
                <Link to="/likes">Likes</Link><t>   </t>

                <div className="Feed">
                    <div className='feed-second' >
                        <button className='showFeed' onClick={this.fetchFeed}>Show Feed</button>
                        <div>
                            <div>
                                {
                                    this.props.feed.map(t =>
                                        <span key={t._id} id={t._id}>
                                            {t.content}
                                            <t> by </t>{t._user.username}
                                            <t>   </t>
                                            {this.checkLike(t.isLiked)}
                                            <hr />
                                        </span>
                                    )
                                }
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
const mapStateToProps = state => ({
    feed: state.feedReducer
})
export default connect(mapStateToProps)(Feed)