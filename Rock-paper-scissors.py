import random

computer_score = 0
your_score = 0

while True :

    choice = input("Enter Your Choice (Rock | Paper | Scissors) :").lower()

    avai_choice = ['Rock','Paper','Scissors']
    com_choice = random.choice(avai_choice).lower() 

    if choice == com_choice:
        print("Tie!")
    else:
        if choice == 'paper' and com_choice == 'rock':
            print('You Won!')
            print('Computer choice is :', com_choice)
            your_score += 1
        elif choice == 'scissors' and com_choice == 'paper':
            print('You Won!')
            print('Computer choice is :', com_choice)
            your_score += 1
        elif choice == 'rock' and com_choice == 'scissors':
            print('You Won!')
            print('Computer choice is :', com_choice)
            your_score += 1
        else:
            print('You lose !')
            computer_score += 1
            print('Computer choice is :', com_choice)

    ans = input('Do you Want to Continue (Y | N)?').lower()

    if ans == 'y':
        continue
    else:
        break

print("Your Score is :", your_score)
print("Computer score is :", computer_score)





