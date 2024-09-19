# Python Quiz App

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question.prompt}")
        for idx, option in enumerate(question.options):
            print(f"{idx+1}. {option}")
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if question.options[user_answer - 1] == question.answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {question.answer}")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid number.")
    
    print(f"\nYour final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    # List of questions
    questions = [
        Question("What is the capital of France?", ["Berlin", "London", "Paris", "Rome"], "Paris"),
        Question("What is 5 + 7?", ["10", "11", "12", "13"], "12"),
        Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars"),
        Question("Who wrote 'Hamlet'?", ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Mark Twain"], "William Shakespeare"),
    ]
    
    print("Welcome to the Quiz App!")
    run_quiz(questions)
