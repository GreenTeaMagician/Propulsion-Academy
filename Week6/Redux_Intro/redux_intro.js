
const iniState = { counter: 0 }

reducer = (state = iniState, action) => {
    switch (action.type) {
        case "more": {
            const newState = { ...state };
            newState.counter++
            return newState
        }
        case "less": {
            const newState = { ...state };
            newState.counter--;
            return newState;
        }
        default:
            return state
    }
};

var increment = () => {
    return store.dispatch({ type: 'more' })
}

let store = Redux.createStore(reducer)

render = () => {
    document.getElementById("counter").innerHTML = store.getState().counter;
};

document.getElementById("more").addEventListener("click", increment);

console.log('hi there!')

document.getElementById("less").addEventListener("click", () => {
    store.dispatch({ type: "less" });
});

store.subscribe(render);
render()

