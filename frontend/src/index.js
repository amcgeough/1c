
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import Example from './App';
import {default as ModalExample} from './App_modal.js';
import QuizApp from './App_quiz';


import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<QuizApp />, document.getElementById('root2'));
ReactDOM.render(<ModalExample />, document.getElementById('root'));

registerServiceWorker();

