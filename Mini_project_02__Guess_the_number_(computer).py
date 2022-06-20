#Guess the number
print("Mini proyect 02: Guess the number game (computer)\n\
Idea from https://www.freecodecamp.org/news/python-projects-for-beginners/\n")


#We'll be using the random library, hence we'll be importing it (see https://docs.python.org/3/library/random.html)
import random
#print(random.randint(1,20))   #Quick test

random_number = random.randint (1,10)
x = int(input ("Guess the number: "))
continue_guessing = True
# We need a condition for if the input is not a number at all
while continue_guessing:
    if random_number == x:
        print (f"Well done!! The number is {x}")
        continue_guessing = False
    elif random_number > x:
        x = int(input ("It is bigger than you think, can you guess? "))
    else:
        x = int(input ("It is smaller than you think, can you guess? "))

print("Thank you for playing")