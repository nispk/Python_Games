import random
from random import randrange

board = [[1,2,3],[4,5,6],[7,8,9]]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("| ",board[i][0]," "," | ",board[i][1]," "," | ",board[i][2],"   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    dict = {1: (0,0) , 2: (0,1) , 3: (0,2) , 4: (1,0) , 5: (1,1) , 6: (1,2) , 7: (2,0) , 8: (2,1) , 9: (2,2)}
    user_move = int(input("Enter your next move: "))
    for key in dict:
        if key == user_move :
            i, j = dict[key][0], dict[key][1]
            board[i][j] = "o"
            
    display_board(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in range(1,9):
                free_fields.append((i,j))
            else:
                continue
    return free_fields
    


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(len(board)):
        if(board[i].count(sign) == 3):
            print("#1 satisfies")
            return True
    for j in range(len(board)):
        if (board[0][j]== sign and board[1][j] == sign and  board[2][j]  == sign):
            print("#2 satisfies for ", j)
            return True
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):
        print("#3 satisfies")
        return True
    elif(board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        print("#4 satisfies")
        return True
        
        

def draw_move(board):
    # The function draws the computer's move and updates the board.
    listl = make_list_of_free_fields(board)
    # print("the listl is " , listl)
    computer_move = random.choice(listl)
    i, j = computer_move
    board[i][j] = "X"
    display_board(board)

print("Let's begin tic-tac-toe")
print("\n")
print("Computer plays the first move")
board[1][1] = "X"
display_board(board)
move = 0

while True:
    enter_move(board)
    move += 1
    if (victory_for(board, "o")):
        print("You Win!")
        break
    elif (move >= 5):
        print("Game over!")
        break
    else:
        draw_move(board)
    if (victory_for(board, "X")):
        print("You lose!")
        break
    else:
        continue
    




    
