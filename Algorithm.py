
#this fie is imported in the 2048_game.py file 
#so that 2048_game.py can access all the functions declared in this file
#importing random package to generate random numbers
import random

#function to initialize the game 

def start():
    #declaring empty game board and adding 4 lists with 4 elements each (as 0)
    board=[]
    for i in range(4):
        board.append([0]*4)

    #printing user controls
    print("The gaming controls are as follows:")
    print("Press '1' to MOVE LEFT")
    print("Press '2' to MOVE RIGHT")
    print("Press '3' to MOVE UP")
    print("Press '4' to MOVE DOWN")
    add_num(board)
    return board

# function to add new 2 or 4 to the board at any random cell
def add_num(board):
    #choosing random row and column
    r= random.randint(0,3)
    c= random.randint(0,3)

    while(board[r][c]!=0):
        r= random.randint(0,3)
        c= random.randint(0,3)

    #the while loop breaks at a position where the board is empty (0)
    #the following adds a random 2 or 4 to the empty cell
    list1 = [2,4]
    board[r][c] = random.choice(list1)


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


#function to compress the board from left to right only, before and after merging of the cells
#for other operations the board will be modified so this function can be used to execute the user commands

def compress(board):

    c=False     #bool variable to keep track of changes made to the board

    #new empty board is created and all elemnts are initialised as (0) or empty
    empty_board=[]        
    for i in range(4):
        empty_board.append([0]*4)

    #shifting every element to the end
    #loop to move through each row
    for i in range(4):
        position =0

        #loop to move through columns/cells of each row
        for j in range(4):

            #if the cell is not empty we will shift it to the previous empty position stored in position variable
            if(board[i][j]!=0):
                empty_board[i][position] = board[i][j]

                if(j!=position):
                    c= True     #changing the flag since a cahnge is being made
                position = position + 1

    return empty_board,c


#function to merge cells after compressing 
#merging occurs if tow cells in are the same then the double of their value is placed in the most extreme cell

def merge(board):

    #again, a bool variable is taken to keep track if any changes are being made to the board after the operation or not
    c=False

    #if current and next cell values are non- zero and same then the current is doubled and the next is made empty
    for i in range(4):
        for j in range(3):
            if(board[i][j]==board[i][j+1] and board[i][j]!=0):
                board[i][j]= ((board[i][j])*2)
                board[i][j+1]=0
                c= True #since change is being made in this conditional statement, the flag is being modified

    return board,c 

#function to reverse the board (matrix) so that the other commands (other than left to right) can be executed 
#by using the compress function that only works for left to right

def reverse(board):

    #a new board is being created to store the reversed board
    empty_board=[]      
    for i in range(4):
        empty_board.append([])
        for j in range(4):
            empty_board[i].append(board[i][3-j])

    return empty_board


#function to transpose the board (matrix) so that the other commands (other than left to right) can be executed 
#by using the compress function that only works for left to right

def transpose(board):

    #empty grid is created to store the transpose of the board 
    empty_board=[]
    for i in range(4):
        empty_board.append([])
        for j in range(4):
            empty_board[i].append(board[j][i])
    return empty_board

#function to update the matrix if the user swipes left

def left(mat):
    #compress the matrix (mat) before merging operation
    new_mat,c1= compress(mat)

    #merge the cells
    new_mat,c2= merge(new_mat)

    #c is a bool var that will store if ANY change is made, either due to merging or just by compressing
    c= c1 or c2 

    #compress after merging operation
    new_mat, t= compress(new_mat)

    #return the new matrix and the bool var to check if a change has taken place or not
    return new_mat,c

#function to update the matrix if the user swipes right

def right(mat):
    #matrix/game board is reverse and stored in a new var
    new_mat = reverse(mat)
    new_mat,c= left(new_mat)        #move left

    #reverse the matrix again to get the final board
    new_mat= reverse(new_mat)
    
    #return the updated board and the bool var to check if any changes were made to the board or not
    return new_mat,c 
#function to update the board if the user swipes up

def up(mat):
    #a new var to store the transposed board/matrix (mat)
    new_mat = transpose(mat)

    #move the transposed matrix to left
    new_mat,c= left(new_mat)

    #transpose the matrix back to get the final result after the operation
    new_mat= transpose(new_mat)

    #return the updated matrix along with the bool flag var
    return new_mat,c

#function to update the board if the user swipes down

def down(mat):
    #new var to store the transposed matrix
    new_mat= transpose(mat)

    #move the transposed matrix to the right 
    #(reverses the matrix and moves it to the left and reverses it back, inside the right() function)
    new_mat,c= right(new_mat)

    #transpose the matrix back to get the final result
    new_mat= transpose(new_mat)
    #return the matrix and the flag variable
    return new_mat,c




