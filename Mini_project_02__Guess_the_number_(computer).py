#Guess the number
print("Mini proyect 02: Guess the number game (computer)\n\
Idea from https://www.freecodecamp.org/news/python-projects-for-beginners/\n")


#We'll be using the random library, hence we'll be importing it (see https://docs.python.org/3/library/random.html)
import random
#print(random.randint(1,20))   #Quick test

def guess(x):
    random_number = random.randint (1,x)
    guess = 0

    #Loop for guessing the number
    while guess != random_number:
        try:        #Condition, guess must be a number or ValueError will raise.
            guess = int(input(f"Guess the number between 1 and {x}: "))
            if random_number > guess:
                print ("It is bigger than you think.")
            elif random_number < guess:
                print ("It is smaller than you think.")
        except ValueError:
            print("Try an integer, please.")
    print (f"\nWell done!! The number is indeed {random_number}.\nThank you for playing this game.")
#Input to guess between 1 and user's choice
try:
    choice = int(input("Give me an integer number: "))
except ValueError:
    print(f"No, not that... an integer (in digits).")
else:
    guess (choice)