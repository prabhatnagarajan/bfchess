from color import *

def even(num):
	return num % 2 == 0

FILES = ['a','b','c','d','e','f','g','h']
RANKS = range(1, 9)
print FILES
print RANKS
SQUARES = []
SQUARE_COLOR = dict()
for file in FILES:
	for rank in RANKS:
		square = str(file) + str(rank)
		SQUARES.append(square)
		file_index = FILES.index(file) + 1
		if (not even(file_index)):
			if even(rank):
				SQUARE_COLOR[square] = Color.WHITE
			else:
				SQUARE_COLOR[square] = Color.BLACK
		else:
			if even(rank):
				SQUARE_COLOR[square] = Color.BLACK
			else:
				SQUARE_COLOR[square] = Color.WHITE		
