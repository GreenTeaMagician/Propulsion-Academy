import { combineReducers } from "redux";
import loginReducer from './loginReducer';
import feedReducer from './feedReducer';
import likeReducer from './likeReducer'

export default combineReducers({
    loginReducer,
    feedReducer,
    likeReducer
});