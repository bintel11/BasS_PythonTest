

import os
import time
import random


numberList = [1,2,3,4,5,6,7,8,9]

#Print the header
def printHeader():
	print ("""
 _____ 
/__ __\   1 | 2 | 3
  / \     4 | 5 | 6
  | |     7 | 8 | 9
  \_/  
                                                            
 Play Tic-Tac-Toe...!
 Your choices are defined, they must be from 1 to 9...!

""")

def playBoard(pboard):
    print(pboard[1],'|',pboard[2],'|',pboard[3])
    print('--+---+--')
    print(pboard[4],'|',pboard[5],'|',pboard[6])
    print('--+---+--')
    print(pboard[7],'|',pboard[8],'|',pboard[9])




def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'P1' or letter == 'P2'):
        print('Do you want to be P1 or P2?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'P1':
        return ['P1', 'P2']
    else:
        return ['P2', 'P1']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'C'
    else:
        return 'P'

def isWin():
    if ((board[1] + board[2] + board[3] == 15) or
        (board[1] + board[4] + board[7] == 15) or
        (board[2] + board[5] + board[7] == 15) or
        (board[3] + board[6] + board[9] == 15) or
        (board[1] + board[5] + board[9] == 15) or
        (board[7] + board[5] + board[3] == 15) or
        (board[4] + board[5] + board[6] == 15) or
        (board[7] + board[8] + board[9] == 15)): 
        
        return True
    else:
        #print ("Player lost!")
        return False


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard



def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpace(board, i):
            return False
    return True

    
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def isSpace(board, pos):
    return board[pos] == 0

def mMove(board, v, p):
    board[p] = v


def isValue(board, value):
    if value in board :
        return False
    else :
        return True



def inputValue (board):
    value = ' '
    while value not in '1 3 5 7 9'.split() or not isValue(board, int(value)):
        print ('Enter value (1-9) :')
        value = input()
    return int(value)

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpace(board, int(move)):
        move = input()       
    return int(move)




def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpace(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def compPlay(board, p2Val):   
    
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpace(copy, i):
            mMove(copy, p2Val, i)
            if isWin():
                return i
            
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

  
def valCp(board):
    
    while True:
        r = random.randrange(2, 10, 2)
        if r not in board :
            choice = r
            break
    return choice

   
while True:
    
    board = ["", 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    gamePlay = True

    
    while gamePlay :
        printHeader()
        playBoard(board)
        print(numberList)
        p1Val = inputValue(board)
        numberList = [ x for x in numberList if x != p1Val]
        print ('Enter position (1-9) :')
        p1Pos = getPlayerMove(board)

        if isSpace(board, p1Pos):
            mMove(board, p1Val ,p1Pos)
            playBoard(board)

        if isWin() :
            print("Player Won !")
            playBoard(board)
            gamePlay = False
            break
        
        if isBoardFull(board):
            playBoard(board)
            print('The game is a tie !')
            break
        
                
        p2Val = valCp(board)
        numberList = [ x for x in numberList if x != p2Val]
        move = compPlay(board, p2Val)
        mMove(board, p2Val, move)
        
        if isWin() :
            print("Computer Won !")
            playBoard(board)
            gamePlay = False
            break
        
        if isBoardFull(board):
            playBoard(board)
            print('The game is a tie !')
            break

    if not playAgain():
        break
        
    
    

    

