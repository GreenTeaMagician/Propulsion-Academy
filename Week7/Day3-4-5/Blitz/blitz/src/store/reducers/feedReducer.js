
/**
 * Post[]
 */

const feedReducer = (state = [], action) => {
    switch (action.type) {
        case "FEED_FETCHED":
            return action.payload;
        default:
            return state;
    }
}
export default feedReducer


