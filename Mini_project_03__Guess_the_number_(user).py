#Guess the number 2
print("Mini proyect 03: Guess the number game (user)\n\
Idea from https://www.freecodecamp.org/news/python-projects-for-beginners/\n")


#We'll be using the random library again
import random

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
        except ValueError:  #because if you don't use a number, when compared it gives error.
            print("Try an integer, please.")
    print (f"\nWell done!! The number is indeed {random_number}.\nThank you for playing this game.")


def computer_guess(x):
    low, high = 1, x
    plow, phigh = low, high
    feedback = "" #Gives the chance to the computer to guess correctly in the first run.
    '''while feedback != "c":
        try:
            guess = random.randint(low,high)
            print ("I chose a number")
        except ValueError:  #because if you lie in feedback, we get randint(a,a), raising error for empty range
            print (f'Are you sure? I think {guess} is correct (C)')

        if high < low: print ("Something went wrong, high can't be lower than low")
        elif high == low: input(f'I think for real it is this number, {guess}, is it correct? (C)')
        else: feedback = input(f' Is {guess} too high (H), too low (L) or correct (C)?? ').lower() 

        if feedback == "h" and high != guess:
            print (high, "H before")
            high = guess - 1    #; print("Oh.. is it?")
        elif feedback == "l" and high != guess:
            print (low, "L before")
            low = guess + 1     #; print ("Oh, I'm getting close")
        """elif feedback != "c":
            print ("I guess I'll try asking  again...")"""
        print (high, "H now")
        print (low, "L now\n")'''

    while feedback != "c" or high < low:
        if high >= low:
            guess = random.randint(low,high)
        else:
            print (f"\nBefore feedback Low was {plow} and high was {phigh}")
            if feedback == 'h':
                print(f"After feedback Low is {low} and high is {high+1} which is not right, let's head back")
                high = phigh
            elif feedback == 'l':
                print(f"After feedback Low is {low-1} and high is {high} which is not right, let's head back")
                low = plow
            guess = random.randint(low,high)
        feedback = input(f'{low}/{high}. Is {guess} (H) (L) or (C): ').lower()
        if feedback == 'h' and (guess-1> low or high>low):
            plow = low
            phigh = high
            high = guess -1
        elif feedback == 'l' and (high> low+1 or high>low):
            plow = low
            phigh = high
            low = guess + 1

    print(f"Yes!! Nice guess, {guess} is the number")

computer_guess(20)
#Sites used for this proyect: 
#  https://docs.python.org/3/library/stdtypes.html