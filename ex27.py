"""
Zed says I should memorize these by writing out index cards.
Why not create a program that does the same thing?
"""

# Run this script by typing in to the bash: $ python3 ex27.py ex27_answerkey.txt

from random import sample
from sys import argv
script, input_file = argv



random_number_list = sample(range(27),10)
print (random_number_list)


# Don't touch this section, it is GOLD!
def print_answer_sheet(f):
    """A function that prints out the answer sheet"""
    print ("Here is the answer sheet:\n\n", f.read())

open_input_file = open(input_file)  # Open the input_file (ex27_answerkey.txt)
print_answer_sheet(open_input_file) # Call function that prints the answer sheet
open_input_file.close()             # Close the input_file

# Add "Beware that your inputs are case sensitive (Capitalize 'T'rue and 'F'alse)"
# Add "while question_count > 1"???
#question_count = 10
#answers_correct = 0
#answers_incorrect = 0
