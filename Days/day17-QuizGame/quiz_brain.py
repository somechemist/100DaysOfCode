class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current = self.question_number
        next = current + 1
        answer = input(f"Q.{next} : {self.question_list[next - 1].text} (True/False)?\n")
        self.question_number = next
        if self.check_answer(answer, self.question_list[next - 1].answer):
            print("Correct")
            self.score += 1
            #print(f"score: {self.score}")
        else:
            print("Incorrect")
            #print(f"score: {self.score}")

    def check_answer(self, u_answer, c_answer):
        return u_answer == c_answer
