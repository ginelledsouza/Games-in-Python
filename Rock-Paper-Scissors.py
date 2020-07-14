"""
Created on Tue Jul 14 

@author: Ginelle
"""

input1 = (input("Welcome to Rock-Paper-Scissors! Would you wish to play? (Yes/No): ")).lower()

while input1 != 'no':
    play1 = (input("Player 1 enter your choice: ")).lower()
    play2 = (input("Player 2 enter your choice: ")).lower()
    #input1 = 'Yes'

    def game(in1,in2):
        if in1 in ['rock','scissors'] and in2 in ['rock','scissors']:
            if in1 == 'rock':
                print("Congratulations to Player 1")
            else:
                print("Congratulations to Player 2")
        elif in1 in ['paper','scissors'] and in2 in ['paper','scissors']:
            if in1 == 'scissors':
                print("Congratulations to Player 1")
            else:
                print("Congratulations to Player 2")
        elif in1 in ['paper','rock'] and in2 in ['paper','rock']:
            if in1 == 'paper':
                print("Congratulations to Player 1")
            else:
                print("Congratulations to Player 2")
        else:
            print("Invalid Entry")

    game(play1,play2)
    input1 = (input("Do you wish to play again? (Yes/No): ")).lower()
