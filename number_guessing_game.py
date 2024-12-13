import random

guesses = 0
random_num = random.randrange(0, 11)

while True:
    guesses += 1
    guess = int(input("Enter a number between 1 and 10: "))

    if random_num == guess:
        print("You guessed correctly!")
        play_again = input("Do you want to play again? Yes(y)/No(n): ")

        if play_again.lower() != "y":
            break
        else:
            continue

    elif random_num < guess:
        print("You crossed the number !")
        continue

    elif random_num > guess :
        print("you are before the number")
        continue

print("Nunmber of guesses is :", guesses)
