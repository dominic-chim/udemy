import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
<<<<<<< HEAD
  ReactDOM.unmountComponentAtNode(div);
=======
>>>>>>> 535c356d4c86e8061a5709aa19ce50b435c58abf
});
