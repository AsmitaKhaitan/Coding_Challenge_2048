
#importing the Algorithm.py file where all the fuctions for the operatins are written
import Algorithm
import numpy as np

#Driver code
if __name__=='__main__':
    #calling start() function to initialize the board
    board= Algorithm.start()
while(True):

    t = input("Enter the number (move) of your choice : ")

    #since 3 is for moving UP
    if(t=='3'):

        #calling the up function to carry out operation
        board,c= Algorithm.up(board)
        #calling function to get the current status of the game
        curr= Algorithm.state(board)
        print(curr)

        #if game is not over then add a random 2 or 4
        if(curr == 'CONTINUE PLAYING, THE GAME IS NOT YET OVER!!!'):
            Algorithm.add_num(board)

        else :
            break

    #the same process like the above if condition is followed for down, left and right
    #since "4" is for moving down 
    elif(t=='4'):
        board,c=Algorithm.down(board)
        curr= Algorithm.state(board)
        print(curr)
        if(curr == 'CONTINUE PLAYING, THE GAME IS NOT YET OVER!!!'):
            Algorithm.add_num(board)

        else :
            break

    #since "1" is for moving left 
    elif(t=='1'):
        board,c=Algorithm.left(board)
        curr= Algorithm.state(board)
        print(curr)
        if(curr == 'CONTINUE PLAYING, THE GAME IS NOT YET OVER!!!'):
            Algorithm.add_num(board)

        else :
            break

    #since "2" is for moving right 
    elif(t=='2'):
        board,c=Algorithm.right(board)
        curr= Algorithm.state(board)
        print(curr)
        if(curr == 'CONTINUE PLAYING, THE GAME IS NOT YET OVER!!!'):
            Algorithm.add_num(board)

        else :
            break
    else:
        print("Invalid choice of move, sorry!")
    #print the board after each move
    print(np.matrix(board))
