

const likeReducer = (state = [], action) => {
    switch (action.type) {
        case "LIKES_FETCHED":
            return action.payload;
        default:
            return state;
    }
}
export default likeReducer
