print("Welcome to My Quiz!")

playing = input("Do you want to play? ").strip().lower()
if playing != "yes":
    quit()

print('''Okay! Let's play (:
There are about 9 questions.''')

score = 0

# Questions and answers stored in a list of dictionaries
questions = [
    {"question": "1. What does CPU stand for? ", "answer": "central processing unit"},
    {"question": "2. What does SU stand for? ", "answer": "system unit"},
    {"question": "3. What does PO stand for? ", "answer": "peter obi"},
    {"question": "4. What does WHO stand for? ", "answer": "world health organization"},
    {"question": "5. What does PC stand for? ", "answer": "personal computer"},
    {"question": "6. Define pi with a number? ", "answer": "3.142"},
    {"question": "7. What does GI stand for? ", "answer": "graphic interface"},
    {"question": "8. Complete the word, SYS? ", "answer": "system"},
    {"question": "9. What does I/O stand for? ", "answer": "input/output"},
]

# Iterate through the list of questions
for q in questions:
    answer = input(q["question"]).strip().lower()
    if answer == q["answer"].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

# Final score and percentage
print(f"You got {score} questions correctly!")
print(f"With a {(score / len(questions)) * 100:.2f}%.")