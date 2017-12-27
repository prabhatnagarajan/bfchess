from constants import *
from color import *
import argparse
import numpy as np
import random
import sys
from pdb import set_trace
import chess

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--piece', choices=["N", "Q", "B", "R"], required=True)
    return parser.parse_args()


def generate_quiz(piece):
    #Quiz is dictionary mapping a problem number to square
    board = chess.Board()
    board.clear_board()
    loc = np.random.randint(64)
    # constants from python-chess api
    if piece == 'N':
        piece_int = chess.KNIGHT
    elif piece == 'B':
        piece_int = chess.BISHOP
    elif piece == 'R':
        piece_int = chess.ROOK
    else:
        piece_int = chess.QUEEN
    dest = np.random.randint(64)
    while (piece == 'B' and SQUARE_COLOR[SQUARES[loc]] != SQUARE_COLOR[SQUARES[dest]]) or (dest == loc):
        dest = np.random.randint(64)

    board.set_piece_at(loc, chess.Piece(piece_int, True))

    set_trace()
    return (quiz, answer_key)

# def calc_distance(board):


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
            print command

def main():
    args = parse_args()
    quizzes = generate_quiz(args.piece)
    print_quizzes(quizzes)

if __name__ == '__main__':
    main()
