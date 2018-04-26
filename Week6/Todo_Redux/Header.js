
// const iniState = { counter: 0 }

// reducer = (state = iniState, action) => {
//     switch (action.type) {
//         case "more":
//             fetch('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
//                 .then(res => res.json())
//                 .then(quotes => { quote: quotes[0] });;
//             return quotes[0]

//         default: {
//             return state
//     }
// };

// var increment = () => {
//     return store.dispatch({ type: 'more' })
// }

// let store = Redux.createStore(reducer)



// document.getElementById("less").addEventListener("click", () => {
//     store.dispatch({ type: "less" });
// });





//--------------------------------------------------------------------------------
console.log('hi');

const initialState = { quoteState: "I just checked your symptoms on the computer, and it seems you have internet connectivity problems" }

var updateQuote = () => {
    return store.dispatch({ type: 'quotePlease' })
};

reducer = (state = initialState, action) => {

    switch (action.type) {
        case "quotePlease": {
            console.log("we are hereeee")
            const newState = { ...state };
            fetch('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
                .then(response => response.json())
                .then(function (quotes) {
                    newState.quoteState = quotes[0]
                    return newState
                })
            }
        default:
            return state
};
}

var fetchQuote = () => {
    fetch('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
        .then(response => response.json())
        .then(function (quotes) {
            console.log('Dominic Decocco')
            initialState.quoteState = quotes[0]
            console.log(quotes[0])
        });
}

let store = Redux.createStore(reducer)

document.getElementById("Header-button").addEventListener("click", updateQuote);
// document.getElementById("more").addEventListener("click", increment);

store.dispatch({ type: 'more' });

var render = () => {
    document.getElementById("quote").innerHTML = store.getState().quoteState
};

store.subscribe(render);
render();