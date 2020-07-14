"""
Created on Tue Jul 14 

@author: Ginelle
"""

def winner_check(games):

    pname = {'X':1, 'O':2}
    
    for i in range(len(games)):
        rscore = 0
        cscore = 0
        dscore = 0
        
        for j in range(len(games[i])):
            if games[i][i] == games[i][j] and games[i][i] in ['X','O']:
                rscore += 1
            if games[i][i] == games[j][i] and games[i][i] in ['X','O']:
                cscore += 1
            if games[i][i] == games[j][j] and games[i][i] in ['X','O']:
                dscore += 1
                
    
        if rscore == len(games):
            winner = games[i][i]
            print()
            print("Player",pname[winner],"wins by Row")
            return 1
            break
        elif cscore == len(games):
            winner = games[i][i]
            print()
            print("Player",pname[winner],"wins by Column")
            return 1
            break
        elif dscore == len(games):
            winner = games[i][i]
            print()
            print("Player",pname[winner],"wins by Diagonal")
            return 1
            break

def show():
    for i in board:
        print(i)
    
    
def moves(rows,cols):
    row = int(move[0]) - 1
    column = int(move[1]) - 1
    return row,column
        
    
lenb = int((input("Enter the dimension on board: ")))
chance = lenb * lenb
board = [(['.']*lenb) for i in range(lenb)]

for i in range(1,chance+1):
    if i%2==0:
        move = input("Enter the row and column you wish to make your move Player 2: ")
        move = move.split(",")
        row,column = moves(move[0],move[1])
        if board[row][column] in ['X','O']:
            print("Play again place taken: ")
            move = input("Enter the row and column you wish to make your move Player 2: ")
            move = move.split(",")
            row,column = moves(move[0],move[1])
            board[row][column] = 'O'
            show()
            final = winner_check(board)
            if final == 1:
                break
        else:
            board[row][column] = 'O'
            show()
            final = winner_check(board)
            if final == 1:
                break
    else:
        move = input("Enter the row and column you wish to make your move Player 1: ")
        move = move.split(",")
        row,column = moves(move[0],move[1])
        if board[row][column] in ['X','O']:
            print("Play again place taken: ")
            move = input("Enter the row and column you wish to make your move Player 1: ")
            move = move.split(",")
            row,column = moves(move[0],move[1])
            board[row][column] = 'X'
            show()
            final = winner_check(board)
            if final == 1:
                break
        else:
            board[row][column] = 'X'
            show()
            final = winner_check(board)
            if final == 1:
                break
            
else:
    print()
    print("No winners. Try again!")




    
    
    