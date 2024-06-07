class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            self.ask_question(question)
        self.display_final_score()

    def ask_question(self, question):
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i+1}. {option}")
        answer = self.get_user_input(question)
        if answer == question.answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is {question.answer}.")

    def get_user_input(self, question):
        while True:
            try:
                user_input = int(input("Enter the number of your answer: "))
                if 1 <= user_input <= len(question.options):
                    return question.options[user_input - 1]
                else:
                    print("Invalid input. Please enter a number between 1 and", len(question.options))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_final_score(self):
        print(f"Your final score is {self.score} out of {len(self.questions)}")

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

# Define the questions
questions = [
    Question("What is the output of the following Python code?\n print('Hello, world!')", ["Hello, world!", "Nothing", "Error", "noneofthese"], "Hello, world!"),
    Question("Which of the following is not a valid data type in Python?", ["Integer","String","Float","Character"], "String"),
    Question("What method is used to remove an item from a list in Python?", ["remove()","pop()","delete()","clear()"], "remove()"),
]

# Create a quiz object and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()