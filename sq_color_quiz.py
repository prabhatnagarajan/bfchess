from constants import *
from color import *
import numpy as np

def generate_quiz():
	#Quiz is dictionary mapping a problem number to square
	sequence = np.random.permutation(np.array(range(NUM_SQUARES)))
	print sequence
	quiz = dict()
	answer_key = dict()
	for num in range(NUM_SQUARES):
		quiz[num] = SQUARES[sequence[num]]
		answer_key[num] = SQUARE_COLOR[SQUARES[sequence[num]]]
	return (quiz, answer_key)

quiz, answer_key = generate_quiz()

quiz_latex =[]
quiz_latex.append("\\subsection {Quiz}")
quiz_latex.append("\\begin{enumerate}")
for num in range(NUM_SQUARES):
	item = "\t \\item "
	item = item + quiz[num]
	quiz_latex.append(item)
quiz_latex.append("\\end{enumerate}")

quiz_latex.append("\\newpage")
quiz_latex.append("\\subsection{Answer Key}")
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

for command in quiz_latex:
	print command