import { createStore, compose, applyMiddleware } from 'redux';
import { persistState } from 'redux-devtools';
import rootReducer from 'reducers';
import logger from 'redux-logger'
import ReduxThunk from 'redux-thunk'


let createStoreWithMiddleware = applyMiddleware(ReduxThunk)(
    applyMiddleware(logger)(createStore)
);

export default function configureStore(initialState) {

  const store = createStoreWithMiddleware(
      rootReducer,
      initialState
  );

  if (module.hot) {
    module.hot.accept('../reducers', () =>
      store.replaceReducer(require('../reducers').default)
    );
  }

  return store;
}
