#Guess the number
print("Mini proyect 02: Guess the number game (computer)\n\
Idea from https://www.freecodecamp.org/news/python-projects-for-beginners/\n")


#We'll be using the random library, hence we'll be importing it (see https://docs.python.org/3/library/random.html)
import random
#print(random.randint(1,20))   #Quick test

def guess(x):
    random_number = random.randint (1,x)
    guess = 0 #A number outside the range to let the player guess.

    #Loop for guessing the number
    while guess != random_number:
        try:        #Condition, guess must be a number or ValueError will raise.
            guess = int(input(f"Guess the number between 1 and {x}: "))
            if random_number > guess:
                print ("It is bigger than you think.")
            elif random_number < guess:
                print ("It is smaller than you think.")
        #If except is left alone, I can not exit the program in the terminal with Ctrl+C (KeyboardInterruption)
        except ValueError:
            print("Try an integer, please.")
    print (f"\nWell done!! The number is indeed {random_number}.\nThank you for playing this game.")


#Input to guess between 1 and user's choice
for i in range (3):
    try:
        choice = int(input("Give me an integer number: "))
    except ValueError:
        answer_list = ["You misunderstood",
         "No, not that... an integer (in digits).",
         "Alright, I'm done"]
        print(answer_list[i])
    else:
        guess (choice)
        break

#Sites used for this proyect: 
#  https://www.w3schools.com/python/python_try_except.asp,
#  https://docs.python.org/3/library/random.html