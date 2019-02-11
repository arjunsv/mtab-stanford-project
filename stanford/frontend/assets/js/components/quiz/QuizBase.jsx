import React from "react";
import {Card, CardBody, CardHeader, CardFooter, Container, Row, Col} from "reactstrap";
import PropTypes from "prop-types";
import { QuizQuestion } from "./QuizQuestion";
import { QuizComplete } from "./QuizComplete";

export class QuizBase extends React.Component {
	componentDidMount() {
		this.quizID = this.props.match.params.quizId;
		// console.log("QuizBase did mount.");
		// console.log(this.quizID);
		this.props.startQuiz(this.quizID);
		this.props.getCategoryData(this.quizID);
		window.scroll(0, 0);
	}

	render() {
		return (
			<div>
			{!this.props.complete ? <QuizQuestion
										categoryId={this.quizID}
										text={this.props.currentQuestion.text}
										answers={this.props.currentQuestion.answers}
										name={this.props.categoryName}
										id={this.props.currentQuestion.id}
										answerQuestion={this.props.answerQuestion}
										media={this.props.currentQuestion.media}
										currentTime={this.props.currentTime}
										timeStarted={this.props.timeStarted}
										maxTime={this.props.maxTime}
										selectedAnswer={this.props.currentQuestion.selectedAnswer}
										selectAnswer={this.props.selectAnswer}
										endQuiz={() => this.props.getCurrentQuestion(this.quizID)}
									/>
									:
									<QuizComplete getResults={this.props.getResults}
										name={this.props.categoryName}
										categoryId={this.quizID}
										num_attempted={this.props.num_attempted}
										num_correct={this.props.num_correct}
										results={ this.props.results }
										submitFeedback={ this.props.submitFeedback}
										outoftime={ this.props.outoftime }
									/>

			}
			</div>
		);
	}
}

QuizBase.propTypes = {
    id: PropTypes.number,
	text: PropTypes.string,
	answers: PropTypes.array,
	category: PropTypes.number,
	categoryName: PropTypes.string,
	num_attempted: PropTypes.number,
	num_correct: PropTypes.number,
	outoftime: PropTypes.bool,
	results: PropTypes.array,
    getCurrentQuestion: PropTypes.func,
    getCategoryData: PropTypes.func,
    answerQuestion: PropTypes.func,
    getResults: PropTypes.func,
    startQuiz: PropTypes.func,
	submitFeedback: PropTypes.func,
	selectAnswer: PropTypes.func
};
