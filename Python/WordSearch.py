words = ["ITALIAN","NOODLES","GEESE","SPAGHETTI","CHEESE","BAGUETT","ROME","PIE","LASAGNA"]
fileName = 'WordSearchTest.txt'
file = open(fileName,'r')

board = []
reversedBoard = []
row = []

for line in file:
    #rstrip to remove the \n and split the line on the \t
    row = line.rstrip().split('\t')
    board.append(row)
file.close()

# https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
#Reflects the board over the y-axis
for r in range(len(board)):
    row = ""
    for rev in range(len(board[r])):
        row +=board[r][rev]
    reversedBoard.append(row[::-1])
print(reversedBoard)

def horizontal(word,wordReverse):
    for r in range(len(board)):
        row = ""
        for c in range(len(board[0])):
            row += board[r][c]
            if word in row:
                print(word, 'is in row', r+1, 'column', row.index(word)+1)
                break
            if wordReverse in row:
                print(wordReverse[::-1], 'is in row', r+1, 'column', row.index(wordReverse)+1)
                break

def vertical(word,wordReverse):
    #rotate the board 90 degrees
    for c in range(len(board)):
        row = ""
        for r in range(len(board[0])-1):
                row += board[r][c]
                if word in row:
                    print(word, 'is in row', row.index(word)+1, 'column',  r+1)
                    break
                if wordReverse in row:
                    print(wordReverse[::-1], 'is in row', r+1, 'column', row.index(wordReverse)+1)
                    break

def diagonal(word,wordReverse):
    for r in range(len(board)):
        row = ""
        for c in range(len(board[0])):
            row += board[r][c]
            if word in row:
                print(word, 'is in row', r+1, 'column', row.index(word)+1)
                return
            if wordReverse in row:
                print(wordReverse[::-1], 'is in row,', r+1, 'column', row.index(wordReverse)+1)
                return
            r += 1
            c += 1
            if r >= (len(board)) or c >= (len(board[0])):
                row = ""
                break
    for c in range(len(board)):
        for r in range(len(board[0])):
            row += board[r][c]
            if word in row:
                print(word, 'is in row', row.index(word)+1, 'column', r+1)
                return
            if wordReverse in row:
                print(wordReverse[::-1], 'is in row,', row.index(wordReverse)+1, 'column', r+1)
                return 
            r += 1
            c += 1
            if r >= (len(board)) or c >= (len(board[0])):
                row = ""
                break
    for r in range(len(reversedBoard)):
        row = ""
        for c in range(len(reversedBoard[0])):
            row += reversedBoard[r][c]
            if word in row:
                print(word, 'is in row', r+1, 'column', row.index(word)+1)
                return
            if wordReverse in row:
                print(wordReverse[::-1], 'is in row,', r+1, 'column', row.index(wordReverse)+1)
                return
            r += 1
            c += 1
            if r >= (len(reversedBoard)) or c >= (len(reversedBoard[0])):
                row = ""
                break
    for c in range(len(reversedBoard)):
        for r in range(len(reversedBoard[0])):
            row += reversedBoard[r][c]
            if word in row:
                print(word, 'is in row', row.index(word)+1, 'column', r+1)
                return
            if wordReverse in row:
                print(wordReverse[::-1], 'is in row,', row.index(wordReverse)+1, 'column', r+1)
                return 
            r += 1
            c += 1
            if r >= (len(reversedBoard)) or c >= (len(reversedBoard[0])):
                row = ""
                break
    
for i in range(len(words)):
    word = words[i]
    wordReverse = word[::-1]
    horizontal(word,wordReverse)
    vertical(word,wordReverse)
    diagonal(word,wordReverse)
