def gameOver(c,board):

	for i in range(3):
		if board[i][0] == c and board[i][1] == c and board[i][2] == c:
			return True
		if board[0][i] == c and board[1][i] == c and board[2][i] == c:
			return True


	if board[0][0] == c and board[1][1] == c and board[2][2]==c:
		return True

	if board[0][2] == c and board[1][1] == c and board[2][0]==c:
		return True

	return False

def moves(board):
	l = []
	for i in range(3):
		for j in range(3):
			if board[i][j] == None:
				l.append((i,j))

	return l


# Function that decides the optimal move using MiniMax Algorithm
def tictactoe(board,turn):

	possible_moves = moves(board)
	if gameOver("X",board):
		return 1,-1,-1
	if gameOver("O",board):
		return -1,-1,-1
	if len(possible_moves) == 0:
		return 0,-1,-1
	
	if turn == "X":
		value = -2
		curr = -2
		for move in possible_moves:
			board[move[0]][move[1]] = "X"
			score,x,y = tictactoe(board,"O")
			curr = max(curr,score)
			if curr > value:
				r = move[0]
				c = move[1]
				value = curr
			board[move[0]][move[1]] = None

	else:
		value = 2
		curr = 2
		for move in possible_moves:
			board[move[0]][move[1]] = "O"
			score,x,y = tictactoe(board,"X")
			curr = min(curr,score)
			if curr < value:
				r = move[0]
				c = move[1]
				value = curr
			board[move[0]][move[1]] = None

	return value,r,c