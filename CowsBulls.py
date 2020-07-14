"""
Created on Tue Jul 14 

@author: Ginelle
"""

import string
import random 

digit = string.digits
randomnum = ''.join(random.choice(digit) for i in range(4))
cows = 0

while cows != 4:
    cows = 0
    bulls = 0
    usernum = input("Enter a 4-Digit number: ")
    for i in range(4):
        if randomnum[i] == usernum[i]:
            cows += 1
        else:
            bulls +=1

    print(cows," Cows, ",bulls,' Bulls')