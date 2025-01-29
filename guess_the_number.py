import random

def guess_the_number():
    print("WELCOME TO GUESS THE NUMBER GAME !")
    print("I have chosen a number between 1 and 100. Can you Guess it ?")

    secret_number=random.randint(1,100)  # Random Number between 1 and 100
    attempts=0

    while True:
        try:
            guess = int(input("Enter your Guess: "))
            attempts +=1 

            if guess < 1 or guess > 100:
                print("Enter Number between 1 and 100")
            elif guess < secret_number:
                print("Entered Number is Too Low ! Try Again.")
            elif guess > secret_number:
                print("Entered Number is Too High ! Try Again.")
            else:
                print("Congratulations ! You Guessed the number right! .")
                break
        except ValueError:
            print("Invalid Input ! Please Enter a Valid Number.")
# Run the Code !
guess_the_number()