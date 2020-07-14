"""
Created on Tue Jul 14 

@author: Ginelle
"""

import random 
again = (input("Welcome! Would you like to play - Any Guesses? (Yes/No): ")).lower()

count = 0

while again == 'yes':
    count += 1
    num = int(input("Enter a number: "))
    rannum = random.randint(1,10)

    print("Input Number:  ",num,"\nRandom Number: ",rannum)

    if num == rannum:
        print("It is a match")
    elif num > rannum:
        print("You have guessed to high. Try again next time!")
    elif num < rannum:
        print("You have guessed to low. Try again next time!")
    else:
        print("There was an error. Try again")
        
    again = (input("Do you wish to play again? (Yes/No): ")).lower()

print()
print("Total number of games played: ",count)