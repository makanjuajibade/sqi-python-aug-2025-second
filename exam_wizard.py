# Project Overview:
# Develop an Exam Wizard program in Python that hardcodes a set of at least 5 theory 
# questions and evaluates the student's answers based on the presence of specific keywords or phrases. The program should ask these questions to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Keywords:
# Create at least 5 theory questions.
# For each question, determine the essential keywords or phrases that should be included in the ideal answer.
# Assign weights to each keyword based on its importance.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Evaluate the user's answers based on the presence of the specified keywords..
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score out of the max score e.g. 10/12.

# Sample Question and Evaluation Criteria:
# Question: Explain the process of photosynthesis.

# Ideal Answer: Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy. It occurs in the chloroplasts of plant cells. The process involves the absorption of light by chlorophyll, the conversion of carbon dioxide and water into glucose and oxygen, and the storage of energy in the form of ATP.

# Keywords and Weights:
# Photosynthesis (2 points)
# Light energy (1 point)
# Chemical energy (1 point)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# ATP (1 point)

# Example of Keyword-Based Marking:
# Student's Answer: Photosynthesis is a process in which plants use sunlight to make 
# food. It happens in the chloroplasts where chlorophyll absorbs light. The plants take in carbon dioxide and water, and produce glucose and oxygen.
# Marked Answer:
# Photosynthesis (2 points)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# Total Score: 9 out of 12 points.



questions = [
        {
            "question": "1. List the six classes of food.",
            "keywords": {"carbohydrate": 1, "protein": 1, "fats and oils" : 1, "mineral salts": 1, "vitamins": 1, "water": 1}
        },
        {
            "question": "2. Define Power?",
            "keywords": {"Power": 1, "rate": 2, "work": 2, "done": 1}
        },
        {
            "question": "3.Explain the process of photosynthesis.",
            "keywords": {"Photosynthesis": 1, "light energy ": 2, "lhlorophyll": 2, "carbon dioxide": 2, "water": 1,"glucose": 1, "oxygen":1}
        },
        {
            "question": "4. List four types of programming languages.",
            "keywords": {"C++": 1, "python": 1, "django": 1, "javascript": 1}
        },
        {
            "question": "5. Explain the purpose of functions in Python.",
            "keywords": {"function": 2, "reuse": 2, "modular": 1}
        }
    ]

def theory_cbt(questions: list[str]):
    total_score = 0

    print("Theory CBT Exam ")
    
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ").lower()
        
        question_score = 0
        for keyword, weight in q["keywords"].items():
            if keyword.lower() in answer:
                question_score += weight
        
        total_score += question_score
        print(f"Score for this question: {question_score}\n")
    
    print(f"Your total score: {total_score}")

theory_cbt(questions)
