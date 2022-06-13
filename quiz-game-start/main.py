from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [
    Question(question["text"], question["answer"]) for question in question_data
]

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    answer = quiz_brain.next_question()
    
print(f"You Scored {quiz_brain.user_score} points out of {quiz_brain.quiz_length} possible")