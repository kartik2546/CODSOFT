import random
questions = {
    "Who was the first Prime Minister of India?": "B",
    "Who was the leader of the Indian independence movement known for his nonviolent resistance?": "C",
    "Which event marked the beginning of the Indian independence movement?": "A",
    "Who was the first female Prime Minister of India?": "D",
    "Which year did India gain independence from British rule?": "C"
}

options = {
    "Who was the first Prime Minister of India?": ["A. Jawaharlal Nehru", "B. Pandit Jawaharlal Nehru", "C. Mahatma Gandhi", "D. Sardar Vallabhbhai Patel"],
    "Who was the leader of the Indian independence movement known for his nonviolent resistance?": ["A. Bhagat Singh", "B. Subhas Chandra Bose", "C. Mahatma Gandhi", "D. Jawaharlal Nehru"],
    "Which event marked the beginning of the Indian independence movement?": ["A. Indian Rebellion of 1857", "B. Salt March", "C. Quit India Movement", "D. Jallianwala Bagh massacre"],
    "Who was the first female Prime Minister of India?": ["A. Sarojini Naidu", "B. Indira Gandhi", "C. Vijaya Lakshmi Pandit", "D. Mother Teresa"],
    "Which year did India gain independence from British rule?": ["A. 1945", "B. 1946", "C. 1947", "D. 1948"]
}
def display_question(question, options):
    print(question)
    for option in options:
        print(option)
    return input("Your answer: ").upper()
def play_quiz():
    score = 0
    for question in random.sample(list(questions.keys()), len(questions)):
        user_answer = display_question(question, options[question])
        if user_answer == questions[question]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", questions[question])
    print("\nQuiz Over!")
    print("Your final score is:", score)
play_quiz()
