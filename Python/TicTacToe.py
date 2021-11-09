import random
print("Welcome to Tic Tac Toe!")

def playerMark():
    player = input("Please pick X or O: ").upper()  #this will be the mark the player chooses
    while True:
        if player == 'X':   #if they pick X
            return player
        elif player == 'O': #if they pick O
            return player
        else:
            player = input("Please pick X or O: ").upper()  #they put anything else than X or O

#prints the board
def printBoard(b):
    for row in range(len(b)):   
        for column in range(len(b[row])):   
            if column != (len(b[row])-1):
                print(b[row][column],end=" | ")
            else:
                print(b[row][column],end="\n")
        if row != (len(b)-1):
            print("-"*9)
    print()

# printBoard(board)
# if board[row][col] == " ":
#     board[row][col] = mark   #reset items in a 2nd list, pull index and reassign

def addMark(m,r,c,b):
    #if the space is blank, add that mark, tell the program we're good
    if b[r][c]==" ":
        b[r][c]=m
        return True
    return False

# addMark(mark,row,col,board)
# printBoard(board)
# board = [[1,2,3],[4,5,6],[7,8,9]]
#cat game   return True if we do have a cat Game

def isFull(board):  #if the board is full of marks
    for i in range(len(board)):
        if " " not in board[i]:
            return True
    return False

#cat game   return True if we do have a cat Game
def catChecker(board):
    #if the board is full then it will be a tie
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == " ":
                return False
    return True

def rowChecker(b):  #checks if there are any wins by the rows
    for r in range(len(b)):
        #to make this more dynamic, I need to iterate through each item in the row
        if b[r][0] != " " and b[r][0] == b[r][1] and b[r][1] == b[r][2]:
            return True
    return False

def colChecker(b):  #checks if there are any wins by the colomns
    for c in range(len(b[0])):
        if b[0][c] != " " and b[0][c] == b[1][c] and b[1][c] == b[2][c]:
            return True
    return False

def diaChecker(b):  #checks if there are any wins by the 2 diagonals
    if b[1][1] != " ":
        #top left to bottom right
        if b[0][0] ==b[1][1] and b[1][1] ==b[2][2]:
            return True
        #top right to bottom left
        elif b[2][0] == b[1][1] and b[1][1] == b[0][2]:
            return True
        return False

def gameOver(b):    #if there is a winner
    # if rowChecker(b) or colChecker(b) or diaChecker(b) are true:  #more efficient for time
    #the line below is a checklist
    if True in [rowChecker(b), colChecker(b), diaChecker(b)]:
        return True
    return False


board = [[" "," "," "],[" "," "," "],[" "," "," "]]

row,col = 0,0
mark = playerMark()
userMark = mark
printBoard(board)
tie = 0
win = 0
lose = 0
while mark != "Q":  #while the user doesn't quit
    correctInput = False    #the user put the right coordinates
    while not correctInput: 
        print()
        if (mark==userMark):    #user says where they want to go
            row=int(input("Which row? "))-1
            col=int(input("Which col? "))-1
        else:                   #computer goes
            row=random.randint(0,2)
            col=random.randint(0,2)
        print()
        if not((0<=row<=2) and (0<=col<=2)):    #coordinates are below 1 or above 3
            print("The row and column are not correct")
        #try to add a mark, and if you do, this is true . . .
        elif not(addMark(mark,row,col,board)):  #the mark is put in a space that has been taken
            print("That space was already taken")
        else:
            correctInput = True

    printBoard(board)
    #if we have a gameOver, set mark to Q and be done with it
    if (gameOver(board)):   #if someone wins
        print(mark, "Wins!")
        if(mark==userMark): #if user wins
            win+=1
        else:       #if the comupter wins
            lose+=1
        ui=input("Do you want to play again? ") #asking to Play again
        if ui.lower()=="no":    #if the user quits
            mark="Q"
        else:                   #if the user plays again
            board=[[" "," "," "],[" "," "," "],[" "," "," "]]
            print(f"""
            Win  {win}
            Lose {lose}
            Tie  {tie} 
            """)
            printBoard(board)
    elif (catChecker(board)):   #if game is a tie
        ui=input("Do you want to play again? ")
        tie+=1
        if ui.lower()=="no":
            mark="Q"
        else:
            board=[[" "," "," "],[" "," "," "],[" "," "," "]]
            print(f"""
            Win  {win}
            Lose {lose}
            Tie  {tie} 
            """)
            printBoard(board)
     #if no game over, then change mark
    elif mark=="X":
          mark="O"
     #if mark was O and no gameOver, change mark
    else:
          mark="X"