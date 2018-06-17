import React, { Component } from 'react';
import update from 'react-addons-update';
//import quizQuestions from './api/quizQuestions';
import Quiz from './components/Quiz';
import Result from './components/Result';
import logo from './svg/logo.svg';
import './App.css';
import EssayForm from './text_area.js'
import MultiSelectField from './Multiselect';
require('react-select/less/default.less')



class QuizApp extends Component {


  render() {
    return (
      <div >
        <EssayForm/>
        <MultiSelectField/>
      </div>
    );
  }

}

export default QuizApp;
