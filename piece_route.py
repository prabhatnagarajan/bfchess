from constants import *
from color import *
import argparse
import numpy as np
import random
import sys
from pdb import set_trace
import chess
import queue

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--piece', choices=["N", "Q", "B", "R"], required=True)
    return parser.parse_args()

def get_piece_int(piece_symbol):
    if piece_symbol == 'N' or piece_symbol == 'n':
        piece_int = chess.KNIGHT
    elif piece_symbol == 'B':
        piece_int = chess.BISHOP
    elif piece_symbol == 'R':
        piece_int = chess.ROOK
    elif piece_symbol == 'Q':
        piece_int = chess.QUEEN
    else:
        raise ValueError("{} not supported yet".format(piece_symbol))
    return  piece_int

def generate_quiz(piece):
    #Quiz is dictionary mapping a problem number to square
    start = np.random.randint(64)
    # constants from python-chess api
    piece_int = get_piece_int(piece)
    dest = np.random.randint(64)
    while (piece == 'B' and SQUARE_COLOR[SQUARES[start]] != SQUARE_COLOR[SQUARES[dest]]) or (dest == start):
        dest = np.random.randint(64)
    return (PIECES[piece_int], chess.SQUARE_NAMES[start], chess.SQUARE_NAMES[dest], num_moves(start, dest, piece_int))

def num_moves(start, dest, piece):
    board = chess.Board()
    squares = queue.Queue()
    squares.put(start)
    visited = set()
    visited.add(start)
    dist = dict()
    dist[start] = 0
    while not squares.empty():
        board.clear_board()
        square = squares.get()
        board.set_piece_at(square, chess.Piece(piece, True))
        neighbors = board.attacks(chess.SQUARES[square])
        for neighbor in neighbors:
            if neighbor == dest:
                return dist[square] + 1
            if neighbor not in visited:
                squares.put(neighbor)
                visited.add(neighbor)
                dist[neighbor] = dist[square] + 1

def check_solution(piece, start_sq_str, dest_sq_str, moves):
    board = chess.Board()
    board.clear_board()
    squares = moves.split()
    assert squares[0] == start_sq_str
    assert squares[len(squares) - 1] == dest_sq_str
    current_square = chess.parse_square(start_sq_str)
    wrong = False
    # check if path is valid
    index = 0
    while not wrong:
        current_square = chess.parse_square(squares[index])
        board.set_piece_at(current_square, chess.Piece(PIECES_TO_INT[piece], True))
        attacked_squares = board.attacks(chess.SQUARES[current_square])
        next_square = chess.parse_square(squares[index + 1])
        if next_square in attacked_squares:
            wrong = False
        else:
            wrong = True
            break
        index += 1
        if index == len(squares) - 1:
            break
    is_valid_path = not wrong
    num_moves_used = len(squares) - 1
    optimal_num_moves = num_moves(chess.parse_square(start_sq_str), chess.parse_square(dest_sq_str), PIECES_TO_INT[piece])
    return is_valid_path, is_valid_path and num_moves_used == optimal_num_moves

def generate_cli_quiz():
    quiz, answer_key = generate_quiz()
    questions = []
    for num in range(NUM_SQUARES):
        questions.append((quiz[num], answer_key[num]))

    wrong = questions[:]
    while wrong:
        questions = wrong[:]
        random.shuffle(questions)
        wrong = []
        for q, a in questions:
            guess = raw_input('%s: ' % q)
            if guess == a:
                print('correct')
            else:
                print('wrong. correct answer: "%s"' % a)
                wrong.append((q, a))


def generate_n_latex_quizzes(n):
    quizzes = []
    for i in range(1, n + 1):
        quizzes.append(generate_latex_quiz(i))
    return quizzes

def generate_latex_quiz(quiz_num):
    quiz, answer_key = generate_quiz()
    quiz_latex =[]
    quiz_latex.append("{\\huge \\textbf{Quiz " + str(quiz_num) + "}}" )
    quiz_latex.append("\\begin{multicols}{3}")
    quiz_latex.append("\\begin{enumerate}")
    for num in range(NUM_SQUARES):
        item = "\t \\item "
        item = item + quiz[num]
        quiz_latex.append(item)
    quiz_latex.append("\\end{enumerate}")
    quiz_latex.append("\\end{multicols}")

    quiz_latex.append("\\newpage")
    quiz_latex.append("{\\huge \\textbf{Answer Key}}")
    quiz_latex.append("\\begin{multicols}{3}")
    quiz_latex.append("\\begin{enumerate}")
    for num in range(NUM_SQUARES):
        item = "\t \\item "
        item = item + quiz[num] + " "
        if answer_key[num] == Color.BLACK:
            item = item + "\\textbf{B}"
        else:
            item = item + "\\textbf{W}"
        quiz_latex.append(item)
    quiz_latex.append("\\end{enumerate}")
    quiz_latex.append("\\end{multicols}")
    quiz_latex.append("\\newpage")

    return quiz_latex

def print_quizzes(quizzes):
    for quiz in quizzes:
        for command in quiz:
            print(command)

def main():
    args = parse_args()
    quiz = generate_quiz(args.piece)
    piece = quiz[0]
    start_sq = quiz[1]
    dest_sq = quiz[2]
    print("Move piece " + piece + " from " + start_sq + " to " + dest_sq)
    solution = input("Write your squares, starting with the original square to the destination, separated by spaces. \n")
    set_trace()
    valid_path, optimal_path = check_solution(piece, start_sq, dest_sq, solution)
    print(valid_path)
    print(optimal_path)
    # print_quizzes(quizzes)

if __name__ == '__main__':
    main()
