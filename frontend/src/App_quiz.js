import React, { Component } from 'react';
import update from 'react-addons-update';
//import quizQuestions from './api/quizQuestions';
import Quiz from './components/Quiz';
import Result from './components/Result';
import logo from './svg/logo.svg';
import './App.css';



class QuizApp extends Component {


constructor(props) {
    super(props);

    this.state = {
          counter: 0,
          quizQuestions: [],
          questionId: 1,
          question: '',
          answerOptions: [],
          answer: '',
          answersCount: {
            Nintendo: 0,
            Microsoft: 0,
            Sony: 0
          },
          result: ''
        };

    this.handleAnswerSelected = this.handleAnswerSelected.bind(this);

  }

  async componentWillMount() {
 //using try and catch due to the api request

    try {
      const res =  await fetch('http://127.0.0.1:8000/api/');
      const choice =  await fetch('http://127.0.0.1:8000/api/choice');
      var quizQuestions1 =  await res.json();
      var quizChoice1 =  await choice.json();

      var i, l, k, j, question_ids=[], choice_ids=[]
      for (i in quizQuestions1) {
      question_ids.push(quizQuestions1[i].id);}

      for (l in quizChoice1) {
      choice_ids.push(quizChoice1[l].id);}

      function text2()
          {
            var full_text="["
            for (j = 0; j < question_ids.length; j++)
                {full_text +=  '{' +
                    '"question": "' + quizQuestions1[j].question_text + '",'
                var question_id = quizQuestions1[j].id
                full_text +=  '"answers": ['
                for (k = 0; k < choice_ids.length; k++)
                    {if (quizChoice1[k].question === question_id)
                        full_text += '{"type": "' + quizChoice1[k].id + '", "content": "' + quizChoice1[k].choice_text + '"},'
                        }
                full_text += ']},'
                        }
          return full_text
          }

      var new1 = text2().replace(/},]}/g, "}]}").replace(/,$/,"]")
      this.state.quizQuestions = JSON.parse(new1);
      console.log(this.state.quizQuestions)

    }
    catch (e) {console.log(e);}


//      const shuffledAnswerOptions = this.state.quizQuestions.map((question) => this.shuffleArray(question.answers));
      const shuffledAnswerOptions = this.state.quizQuestions.map((question) => this.shuffleArray(question.answers));

      this.setState({
       question: this.state.quizQuestions[0].question,
       answerOptions: shuffledAnswerOptions[0]
        });
}


  shuffleArray(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) {

      // Pick a remaining element...
//      randomIndex = Math.floor(Math.random() * currentIndex);
// AMG Stop shuffle silliness
      randomIndex = Math.floor(Math.random() * 1);
      currentIndex -= 1;

      // And swap it with the current element.
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }

    return array;
  };

  handleAnswerSelected(event) {

    this.setUserAnswer(event.currentTarget.value);

    if (this.state.questionId < this.state.quizQuestions.length) {
        setTimeout(() => this.setNextQuestion(), 300);
    } else {
        setTimeout(() => this.setResults(this.getResults()), 300);
    }
  }

  setUserAnswer(answer) {
    const updatedAnswersCount = update(this.state.answersCount, {
      [answer]: {$apply: (currentValue) => currentValue + 1}
    });

    this.setState({
        answersCount: updatedAnswersCount,
        answer: answer
    });
  }

  setNextQuestion() {

    const counter = this.state.counter + 1;
    const questionId = this.state.questionId + 1;

    this.setState({
        counter: counter,
        questionId: questionId,
        question: this.state.quizQuestions[counter].question,
        answerOptions: this.state.quizQuestions[counter].answers,
        answer: ''
    });
  }

  getResults() {
    const answersCount = this.state.answersCount;
    const answersCountKeys = Object.keys(answersCount);
    const answersCountValues = answersCountKeys.map((key) => answersCount[key]);
    const maxAnswerCount = Math.max.apply(null, answersCountValues);

    return answersCountKeys.filter((key) => answersCount[key] === maxAnswerCount);
  }

  setResults(result) {
    if (result.length === 1) {
      this.setState({ result: result[0] });
    } else {
      this.setState({ result: 'Finished' });
    }
  }

  renderQuiz() {

    return (
      <Quiz
        answer={this.state.answer}
        answerOptions={this.state.answerOptions}
        questionId={this.state.questionId}
        question={this.state.question}
        questionTotal={this.state.quizQuestions.length}
        onAnswerSelected={this.handleAnswerSelected}
      />
    );
  }

  renderResult() {
    return (
      <Result quizResult={this.state.result} />
    );
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>First Compliance</h2>
        </div>
        {this.state.result ? this.renderResult() : this.renderQuiz()}
      </div>
    );
  }

}

export default QuizApp;
