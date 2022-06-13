class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.quiz_length = len(self.question_list)
        self.user_score = 0


    def still_has_questions(self):
        return self.question_number < self.quiz_length

    def next_question(self):
        current_question = self.question_list[self.question_number]
        text = current_question.text
        correct_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {text} (True/False)\n")
        self.check_answer(user_answer,correct_answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("CORRECT!")
            self.score_points()
        else:
            print("WRONG!")
