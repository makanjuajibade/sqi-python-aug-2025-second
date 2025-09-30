# Project Overview:
# Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of 
# at least 5 objective questions and their answers. The program should ask these questions 
# to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score.



questions = [
    {
        "question": "What sound does a cow make?",
        "options": ["A. Meow", "B. Bark", "C. Moo", "D. Quack"],
        "answer": "C"
    },
    {
        "question": "How many legs does a spider have?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "B"
    },
    {
        "question": "All the following are primary colours except?",
        "options": ["A. Yellow", "B. Green", "C. Red", "D. Blue"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 4"],
        "answer": "D"
    },
    {
        "question": "What us the colour of the sky on a clear day?",
        "options": ["A. Yellow", "B. Black", "C. Blue", "D. Red"],
        "answer": "C"
    },
    {
        "question": "What is the capital of England?",
        "options": ["A. London", "B. Tokyo", "C. Abuja", "D. Doha"],
        "answer": "A"
    }
    
]

def cbt_exam(questions):
    score = 0
    print("Welcome to the CBT exam")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        for options in q['options']:
            print(options)
        
        answer = input("Enter your answer A/B/C/D: ")
        
        if answer == q["answer"]:
            print("Correct")
            score += 1

        else:
            print("Wrong Answer") 

    print(f"Test completed. Your score is {score}")

cbt_exam(questions)