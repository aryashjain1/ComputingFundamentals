from random import randint

answer = randint(1, 1000)

play_again = ""

while (play_again != "n"):
    guess = int(input("Enter a number between 1 and 1000: "))
    if guess == answer:
        play_again = input("Congratulations. You guessed the number! Would you like to play again (y/n)? ")
        answer = randint(1,1000)
    elif guess > answer:
        print("Too high. Try again")
    else:
        print("Too low. Try again")
