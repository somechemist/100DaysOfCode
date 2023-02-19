#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create the question bank from the data
question_bank = []
for q in question_data:
    question_bank.append(Question(q['question'], q['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("The quiz is over")
print(f"Your score was {quiz.score}/{quiz.question_number}")