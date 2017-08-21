from color import *

def even(num):
    return num % 2 == 0

def get_rank(square):
    return int(square[1])

class Square:
    def Square(self, file, rank):
        self.file = file
        self.rank = rank

    def getString(self):
        return str(self.file) + str(self.rank)

FILES = ['a','b','c','d','e','f','g','h']
RANKS = range(1, 9)
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

NUM_SQUARES = 64

#Diagonals
DIAGONALS = []
DIAGONAL_COLOR = dict()
DIAGONAL_LENGTH = dict()

DIAGONALS.append(('a1','h8'))
DIAGONALS.append(('b1','h7'))
DIAGONALS.append(('c1','h6'))
DIAGONALS.append(('d1','h5'))
DIAGONALS.append(('e1','h4'))
DIAGONALS.append(('f1','h3'))
DIAGONALS.append(('g1','h2'))
DIAGONALS.append(('h1','h1'))

DIAGONALS.append(('a1','h8'))
DIAGONALS.append(('a2','g8'))
DIAGONALS.append(('a3','f8'))
DIAGONALS.append(('a4','e8'))
DIAGONALS.append(('a5','d8'))
DIAGONALS.append(('a6','c8'))
DIAGONALS.append(('a7','b8'))
DIAGONALS.append(('a8','a8'))

DIAGONALS.append(('a1','a1'))
DIAGONALS.append(('a2','b1'))
DIAGONALS.append(('a3','c1'))
DIAGONALS.append(('a4','d1'))
DIAGONALS.append(('a5','e1'))
DIAGONALS.append(('a6','f1'))
DIAGONALS.append(('a7','g1'))
DIAGONALS.append(('a8','h1'))

DIAGONALS.append(('a8','h1'))
DIAGONALS.append(('b8','h2'))
DIAGONALS.append(('c8','h3'))
DIAGONALS.append(('d8','h4'))
DIAGONALS.append(('e8','h5'))
DIAGONALS.append(('f8','h6'))
DIAGONALS.append(('g8','h7'))
DIAGONALS.append(('h8','h8'))

for diagonal in DIAGONALS:
    DIAGONAL_COLOR[diagonal] = SQUARE_COLOR[diagonal[0]]

for diagonal in DIAGONALS:
    rank1 = get_rank(diagonal[0])
    rank2 = get_rank(diagonal[1])
    DIAGONAL_LENGTH[diagonal] = abs(rank1 - rank2) + 1

