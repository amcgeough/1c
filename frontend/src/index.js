import React from 'react';
import ReactDOM from 'react-dom';
//import './index.css';
//import Example from './App';
//import {default as ModalExample} from './App_modal.js';
import SelectTool from './select_tool';

import registerServiceWorker from './registerServiceWorker';


//ReactDOM.render(<QuizApp />, document.getElementById('root2'));
ReactDOM.render(<SelectTool />, document.getElementById('root'));


registerServiceWorker();

