
#importing random package to generate random numbers
import random

#function to initialize the game 

def start():
    #declaring empty game board and adding 4 lists with 4 elements each (as 0)
    board=[]
    for i in range(4):
        board.append([0]*4)

    #printing user controls
    print("The gaming controls are as follos:")
    print("Press '1' to MOVE LEFT")
    print("Press '2' to MOVE RIGHT")
    print("Press '3' to MOVE UP")
    print("Press '4' to MOVE DOWN")

    add_num(board)
    return board

# function to add new 2 or 4 to the board at any random cell
def add_num(board):
    #choosing random row and column
    r= random.rnadint(0,3)
    c= random.rnadint(0,3)

    while(board[r]!=0):
        r= random.rnadint(0,3)
        c= random.rnadint(0,3)

    #the while loop breaks at a position where the board is empty (0)
    #the following adds a random 2 or 4 to the empty cell
    list1 = [2,4]
    board[r] = random.choice(list1)


#function to check state of game (won/lost/unfinished)
def state(board):

    #goal of the game is to reach the number 2048
    for i in range(4):
        for j in range(4):
            if(board[i][j]==2048):
                return '!!CONGRATULATIONS!! YOU WON!!'

    #if even one of the cells is empty (0) then the game is not over
    for i in range(4):
        for j in range(4):
            if(board[i][j]==0):
                return 'CONTINUE PLAYING, THE GAME IS NOT YET OVER!!!'
    #if no space is empty but after any move two or more cells can merge then the game is not over yet
    for i in range (3):
        for j in range(3):
            if(board[i][j]==board[i+1][j] or board[i][j]==board[i][j+1]):
                return 'CONTINUE PLAYING, THE GAME IS NOT YET OVER!!!'
    for k in range(3):
        if(board[3][k]==board[3][k+1]):
            return 'CONTINUE PLAYING, THE GAME IS NOT YET OVER!!!'
    for i in range(3):
        if(board[i][3]==board[i+1][3]):
            return 'CONTINUE PLAYING, THE GAME IS NOT YET OVER!!!'

    return 'SORRY Y0U LOST !! :('
