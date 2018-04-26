const initialState = {
    counter: 0,
  };

  counterReducer = (state = initialState, action) => {
    switch (action.type) {
      case "up": {
          const newState = { ...state };
          newState.counter++
          return newState
      }
      case "down": {
          const newState = { ...state };
          newState.counter--;
          return newState;
      }
      default: 
       return state
    }
  };

  let store = Redux.createStore(counterReducer);

  render = () => {
    document.getElementById("counter").innerHTML = store.getState().counter;
  };

  document.getElementById("up").addEventListener("click", () => {
    store.dispatch({ type: "up" });
  });

  document.getElementById("down").addEventListener("click", () => {
    store.dispatch({ type: "down" });
  });

  store.subscribe(render);
  render();