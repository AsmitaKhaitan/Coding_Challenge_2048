
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

