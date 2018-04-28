export const loginReducer = (data) => ({
    type: "LOGIN_CORRECT",
    payload: data,
});

export const fetchFeedAction = (data) => ({
    type: "FEED_FETCHED",
    payload: data
})

export const fetchLikesAction = (data) => ({
    type: "LIKES_FETCHED",
    payload: data
})

export const login = (data) => (dispatch, getState) => {
    const myHeaders = new Headers({
        'content-type': 'application/json'
    });
    const config = {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify(data)
    };

    fetch('https://propulsion-blitz.herokuapp.com/api/login', config)
        .then(
            res => {
                if (!res.ok) {
                    console.log(this.props);
                    // this.props.LogResponse = 'You are now logged in!'
                    console.log(res);
                    return;
                }
                return res.json();
            }
        )
        .then(data => {
            if (data !== undefined) {
                localStorage.setItem('token', data.token);
                localStorage.setItem('email', data.email);
                // localStorage.setItem('currentUser', data.email);
            }

            // console.log(localStorage.getItem('token'))
            // console.log(localStorage.getItem('data'))
        })
}

export const fetchFeed = (data) => (dispatch, getState) => {

    const myHeaders = new Headers({
        Authorization: `Bearer ${localStorage.getItem('token')}` // this is the recommended header if you are using JWT
    });

    const config = {
        method: 'GET',
        headers: myHeaders,
    };
    fetch(`https://propulsion-blitz.herokuapp.com/api/feed`, config)
        .then(response => {
            if (response.status.ok) {
                return
            }
            return response.json();
        })
        .then(data => dispatch(fetchFeedAction(data)))
}

export const fetchLikes = (data) => (dispatch, getState) => {
    const myHeaders = new Headers({
        Authorization: `Bearer ${localStorage.getItem('token')}` // this is the recommended header if you are using JWT
    });

    const config = {
        method: 'GET',
        headers: myHeaders,
    };

    fetch(`https://propulsion-blitz.herokuapp.com/api/feed`, config)
        .then(response => {
            if (response.status.ok) {
                // console.log('sdfdfgs');
                return
            }
            console.log(response);
            return response.json();
        })
        .then(data => {
            console.log(data)
            dispatch(fetchLikesAction(data)
        )
    })
}
