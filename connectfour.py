def createBoard():
    r, c = 6, 7
    if 'n' == input('Standard game? (y/n): '):
        r, c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    return [['·'] * c for i in range(r)]

def printBoard(board):
    r, c = len(board), len(board[0])
    spaces = 1
    if r>9 or c>9: spaces = 2 #bigBoard
    x = ''
    for row in range(r-1,-1, -1): #count backward
        x += f'{row:>{spaces}}' # (' '+lastnumber)+... + (' '+0)
        ss = ' '
        if spaces==2: ss = '  '
        for col in range(c):
            x += ss+board[row][col] 
        x += ' \n'
    x += ' ' + ' '*spaces
    for col in range(c): 
        x += f'{col:>{spaces}}'+' '
    print(x)

def makeMove(board, player, col):
    # if col.isdecimal() == False:
    #     printBoard(board)
    #     move = input( 'player'+player+' (col #): ')
    #     if move == 'e':
    #         return False
    #     makeMove(board, player, move)
    
    r = len(board)
    try:
        col = int(col)
        for row in range(r):
            if board[row][col]!='·' and board[row+1][col]=='·':
                board[row+1][col] = player
                break
            elif board[row][col]=='·':
                board[row][col] = player
                break
    except: #to handle if the column is full
        printBoard(board)
        move = input( 'player'+player+' (col #): ')
        if move == 'e':
            return False
        makeMove(board, player, move)
        
def win(player, board):
    row = len(board)
    col = len(board[0])
    for a in range(row):
        for b in range(col-3): 
            if board[a][b] == player and board[a][b+1] == player and board[a][b+2] == player and board[a][b+3] == player:
                return True #horizontal
    
    for a in range(row-3):
        for b in range(col):        
            if board[a][b] == player and board[a+1][b] == player and board[a+2][b] == player and board[a+3][b] == player:
                return True #vertical

    for a in range(row-3):
        for b in range(col-3):  
            if board[a][b] == player and board[a+1][b+1] == player and board[a+2][b+2] == player and board[a+3][b+3] == player:
                return True #diagonal increasing
    
    for a in range(row-3):
        for b in range(col):
            if board[a][b] == player and board[a+1][b-1] == player and board[a+2][b-2] == player and board[a+3][b-3] == player:
                return True #diagonal decreasing

def tie(board):
    row = len(board)
    col = len(board[0])
    for a in range(row):
        for b in range(col):
            if board[a][b] == '·':
                return False
    return True
    
board = createBoard() #contains the dot [...], [...]
printBoard(board)
player = 'X'
while True:
    move = input( 'player'+player+' (col #): ')
    if move == 'e': 
        break

    mm = makeMove(board, player, move)
    if mm == False:
        break

    printBoard(board)
    if win(player, board):
        print('Player', player, 'has won!')
        break
    if tie(board):
        print('Draw!')
        break
    if player == 'X': 
        player = 'O'
    else: 
        player = 'X'
print('bye')