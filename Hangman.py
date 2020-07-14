"""
Created on Tue Jul 14 

@author: Ginelle
"""

import random
def hangman(num):
    if j == 1:
        print()
        print(" _")
        print("| |")
        print("  O")
        print()
    elif j == 2:  
        print()
        print(" _")
        print("| |")
        print("  O")
        print("  |")
        print()
    elif j == 3:
        print()
        print(" _")
        print("| |")
        print("  O")     
        print("  |/")
        print()
    elif j == 4:    
        print()
        print(" _")
        print("| |")
        print("  O")     
        print(" \|/")
        print()
    elif j == 5:
        print()
        print(" _")
        print("| |")
        print("  O")
        print(" \|/")
        print('   \,')
        print()
    else:
        print()
        print(" _")
        print("| |")
        print("  O")
        print(" \|/")
        print(",/ \,\n")
        print("Sorry man is hung!")
        

print("Welcome to Hangman!")

with open('Desktop\words.txt','r') as file:
    words = file.read()
    words = words.split("\n")

word = random.choice(words)

chance = 0
words = list(word)
gword = list("_"*len(word))
gList = []
guessed = ''
j = 1

print("The word you have to guess is as follows \n","_ "*len(word))
print()

while chance < 6:
    
    if guessed == word:
        break
    lasttry = 0
    hangtry = 0
    left = 6 - chance
    print("You have {} chance Left\n".format(left))
    if left == 1:
       option = (input("This is your last attempt. Have you figured the word? (Yes/No): ")).upper()
       if option == 'YES':
           last = (input("Enter the word: ")).upper()
           word = word.upper()
           if last == word:
               print("Congratulation you won!")
               lasttry = 1
               break
           else:
               print("Sorry you lost. The word is incorrect!")
               lasttry = 1
               break
        
    guess =  (input("Enter a letter: ")).upper()
    
    if guess in gList:
        print("The letter exists.\n")
        
    elif guess in words:
        gList.append(guess)
        for i in range(len(words)):
            if guess in words[i]:
                gword[i] = guess
        guessed = "".join(gword)
        print(guessed,"\n")
    else:
        hangman(j)
        j += 1    
        chance += 1

if lasttry == 0 and hangtry == 0:
    if (guessed).upper() == (word).upper():
        print()
        print("Congratulation you won!")
    else:
        print()
        print("Sorry you lost as you have exhausted your attempts!")
        print("The Word was: ",(word).upper())