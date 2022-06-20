#print( "Hello there!" )
#Seguiré ideas de proyectos de la siguiente URL: https://www.freecodecamp.org/news/python-projects-for-beginners/
#Deseenme suerte!!

#1 Mad Libs     #string concatenation

dessert_name = "Apples" #string variable
some_number = 5

#Some ways to concatenate strings
print ("Hello there, I'd love " + str(some_number) + " juicy " + dessert_name) #can only concatenate str to str
print ("Hello there, I'd love", some_number, "juicy", dessert_name)            #can concatenate != data types
print ("Hello there, I'd love {} juicy {}".format(some_number, dessert_name))  #old way of formatted string literal
print (f"Hello there, I'd love {some_number} juicy {dessert_name}")            #new way of formatted string literal, more straightforward or readable
#print(f"{}") is the cleanest way to express string concatenation

"""
adj1 = input("Adjetivo: ")
adj2 = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo infinitivo: ")
verb3 = input("Verbo conjugado: ")
name1 = input("Nombre: ")


madlib = f"Programar es tan {adj1}! Puedo escribir lo que quiera y {verb1} mucho\n"\
    f"Me siento {adj2} y quiero {verb2}. No olvides tomar agua {name1} y tomar descansos\n"\
    f"Ojalá te pongas bien y {verb3}"

print (madlib)
"""

name1 = input ("Person's Name: ")       #1
noun1 = input ("Noun: ")                #2
adj1 = input ("Feeling: ")              #3
verb1 = input ("Verb: ")                #4
adj2 = input ("Feeling: ")              #5
anim1 = input ("Animal: ")              #6
verb2 = input ("Verb: ")                #7
color1 = input ("Color: ")              #8
verb3 = input ("Verb ending in ing: ")  #9
adverb1 = input ("Adverb ending in ly: ")   #10
numb1 = input ("Number: ")              #11
time1 = input ("Measure of time: ")       #12
color2 = input ("Color: ")              #13
anim2 = input ("Animal: ")              #14
numb2 = input ("Number: ")              #15
silw1 = input ("Silly word: ")          #16
noun2 = input ("Noun: ")                #17

#Can I put all these variables in a list? how can I profit from it?
#Mad Libs: A camping We Will Go!
madlib2 = f"This weekend I am going camping with {name1}. I packed my lantern, sleeping bag and {noun1}. I am so {adj1} to {verb1} in a tent. \
I am {adj2} we might see a {anim1}, they are kind of dangerous. We are going to hike, fish and {verb2}. I have heard that the {color1} lake is great for {verb3}. \
Then we will {adverb1} hike through the forest for {numb1} {time1}. If I see a {color2} {anim2} while hiking, I am going to bring it home as a pet! \
At night we will tell {numb2} {silw1} stories and roast {noun2} around the campfire!!"

print (madlib2)
print ("\nBorrowed from the site: https://www.thepaintedturtle.org/sites/main/files/file-attachments/mad_libs.pdf")
