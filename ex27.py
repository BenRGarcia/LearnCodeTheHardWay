"""
Zed says I should memorize these by writing out index cards.
Why not create a program that does the same thing?
FYI, Run this script with: $ python3 ex27.py ex27_answerkey.txt
"""
from random import sample
#from sys import argv
#script, input_file = argv

question_count = int(input("How many questions would you like in this quiz? "))
random_numbers = sample(range(27),question_count)

print (random_numbers)

question_bank = [
("not False", "True"),
("not True", "False"),
("True or False", "True"),
("True or True", "True"),
("False or True", "True"),
("False or False", "False"),
("True and False", "False"),
("True and True", "True"),
("False and True", "False"),
("False and False", "False"),
("not(True or False)", "False"),
("not(True or True)", "False"),
("not(False or True)", "False"),
("not(False or False)", "True"),
("not(True and False)", "True"),
("not(True and True)", "False"),
("not(False and True)", "True"),
("not(False and False)", "True"),
("1 != 0", "True"),
("1 != 1", "False"),
("0 != 1", "True"),
("0 != 0", "False"),
("1 == 0", "False"),
("1 == 1", "True"),
("0 == 1", "False"),
("0 == 0", "True")
]

#res_list = [x[0] for x in question_bank]
#print (res_list[-1])

while question_count > 0:
    question = question_bank[random_numbers.pop(0)]
    print ("Does the following expression result in True or False?\n", question[0])
    #print ("Does the following expression result in True or False? %s" % question)
    answer = input("\t>")
    question_count -= 1

#-------------------------------------------------
"""
def logic_quiz():
    for q in question_bank:
        print (q[0])

logic_quiz()
"""
#for logical_expression, true_or_false in logic_quiz_question_bank:

# Add "Beware your inputs are case sensitive (Capitalize 'T'rue and 'F'alse)"
# Add "while question_count > 1"???
#-------------------------------------------------------------------------------
"""
import ex27_question_bank # This line works now--don't break it

def logic_quiz():
    question_list = [
    ex27_question_bank.question_1(),
    ex27_question_bank.question_2(),
    ex27_question_bank.question_3(),
    ex27_question_bank.question_4(),
    ex27_question_bank.question_5(),
    ex27_question_bank.question_6(),
    ex27_question_bank.question_7(),
    ex27_question_bank.question_8(),
    ex27_question_bank.question_9(),
    ex27_question_bank.question_10(),
    ex27_question_bank.question_11(),
    ex27_question_bank.question_12(),
    ex27_question_bank.question_13(),
    ex27_question_bank.question_14(),
    ex27_question_bank.question_15(),
    ex27_question_bank.question_16(),
    ex27_question_bank.question_17(),
    ex27_question_bank.question_18(),
    ex27_question_bank.question_20(),
    ex27_question_bank.question_21(),
    ex27_question_bank.question_22(),
    ex27_question_bank.question_23(),
    ex27_question_bank.question_24(),
    ex27_question_bank.question_25(),
    ex27_question_bank.question_26(),
    ]
    quiz_list = question_list[random_number_list]
    """
#-------------------------------------------------------------------------------
"""
def print_answer_sheet(f):
    #A function that prints out the answer sheet
    print ("Here is the answer sheet:\n\n", f.read())

open_input_file = open(input_file)  # Open the input_file (ex27_answerkey.txt)
print_answer_sheet(open_input_file) # Call function that prints the answer sheet
open_input_file.close()             # Close the input_file
"""

"""
def logic_quiz():
    question_list = [
    ex27_question_bank.question_1(),
    ex27_question_bank.question_2(),
    ex27_question_bank.question_3(),
    ex27_question_bank.question_4(),
    ex27_question_bank.question_5(),
    ex27_question_bank.question_6(),
    ex27_question_bank.question_7(),
    ex27_question_bank.question_8(),
    ex27_question_bank.question_9(),
    ex27_question_bank.question_10(),
    ex27_question_bank.question_11(),
    ex27_question_bank.question_12(),
    ex27_question_bank.question_13(),
    ex27_question_bank.question_14(),
    ex27_question_bank.question_15(),
    ex27_question_bank.question_16(),
    ex27_question_bank.question_17(),
    ex27_question_bank.question_18(),
    ex27_question_bank.question_20(),
    ex27_question_bank.question_21(),
    ex27_question_bank.question_22(),
    ex27_question_bank.question_23(),
    ex27_question_bank.question_24(),
    ex27_question_bank.question_25(),
    ex27_question_bank.question_26(),
    ]

#question_list[0]
"""
