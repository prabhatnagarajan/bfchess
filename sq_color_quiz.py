from constants import *
from color import *
import argparse
import numpy as np
import random
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    quiz_type = parser.add_mutually_exclusive_group(required=True)
    quiz_type.add_argument('--cli', action='store_true')
    quiz_type.add_argument('--latex', action='store_true')
    return parser.parse_args()


def generate_quiz():
    #Quiz is dictionary mapping a problem number to square
    sequence = np.random.permutation(np.array(range(NUM_SQUARES)))
    quiz = dict()
    answer_key = dict()
    for num in range(NUM_SQUARES):
        quiz[num] = SQUARES[sequence[num]]
        answer_key[num] = SQUARE_COLOR[SQUARES[sequence[num]]]

    return (quiz, answer_key)


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
    quizzes = generate_n_latex_quizzes(int(sys.argv[1]))
    print_quizzes(quizzes)

if __name__ == '__main__':
    main()
