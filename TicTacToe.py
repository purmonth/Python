import random

board = [' ' for x in range(10)]

#check the space is free or not
def spaceIsFree(position):
	return board[position] == ' '

def insertBoard(letter, position):
	global board
	board[position] = letter
	

#draw the board
def drawBoard(board):
	print('   |   |   ')
	print(' '+board[1]+' | '+board[2]+' | ' +board[3]+ ' ')
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(' '+board[4]+' | '+board[5]+' | ' +board[6]+ ' ')
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(' '+board[7]+' | '+board[8]+' | ' +board[9]+ ' ')
	print('   |   |   ')


def insertPlayerLetter():
	#let the player be which letter he want to be
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Which letter you want to be X or O ?')
		letter = input().upper()

		if letter == 'X':
			return ['X','O']
		else:
			return ['O','X']


def isWinner(board, letter):
	return (
		(board[1] == letter and board[2] == letter and board[3] == letter) or
		(board[4] == letter and board[5] == letter and board[6] == letter) or
		(board[7] == letter and board[8] == letter and board[9] == letter) or
		(board[1] == letter and board[4] == letter and board[7] == letter) or
		(board[2] == letter and board[5] == letter and board[8] == letter) or
		(board[3] == letter and board[6] == letter and board[9] == letter) or
		(board[1] == letter and board[5] == letter and board[9] == letter) or
		(board[3] == letter and board[5] == letter and board[7] == letter)
		)



def playerMove(letter):
	move = input('Please select a position to place ~ (1~9) ')
	try:
		move = int(move)
		if move > 0 and move < 10:
			if spaceIsFree(move):
				run = False
				insertBoard(letter,move)
			else:
				print('This position is already occupied!')
		else:
			print('Please type a number within the range!')
	except:
		print('Please type a number!')



def selectRandom(board):
	pass

def isBoardFull(board):#judge the board is full or not

	if board.count(' ') > 1:
		return False
	else:
		return True

def main():
	insertPlayerLetter()
	drawBoard(board)
	while not(isBoardFull(board)):
		if (isWinner(board,'X')):
			print('X win this time ~')
			break
		else:
			playerMove('O')
			drawBoard(board)


		if (isWinner(board,'O')):
			print('O win this time ~')
			break

		else:
			playerMove('X')
			drawBoard(board)

main()

while True:
	answer = input('Do you want to play again ? (Y/N)')
	if answer.lower() == 'y' or answer.lower() == 'yes':
		board = [' ' for x in range(10)]
		print('-------- next round -------')
		main()
	else:
		break


