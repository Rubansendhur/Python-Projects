print("Welcome To The Computer Quiz Game!")

playing = input("Do you want to play? Yes(y)/No(n): ")
score = 0

if playing.lower() != "Y" and playing != "y":
    quit()
else:

    print("Let's play! :)")
    questions = ['What does CPU stand for? ', 'What does GPU stand for? ', 'What does RAM stand for? ', 'What does PSU stand for? ', 'What does HDD stand for? ']

    answers = ['Central Processing Unit', 'Graphics Processing Unit', 'Random Access Memory', 'Power Supply Unit', 'Hard Disk Drive']

    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]}")
        answer = input("Your answer: ").lower()
        if answer == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"Your score is {score} out of {len(questions)}")
    print(f"Your percentage score is {score/len(questions) * 100}%")

    if score == len(questions):
        print("Congratulations! You got all the answers correct!")
    else:
        print("Better luck next time!")