### a quiz app for SKT

question_list = []
answer_list = [[]]
option_letter = ["A. ", "B. ", "C. ", "D. "]

def add_question(question, answer, !a1, !a2, !a3):
    question_list.append(question)
    answer_list.append(answer)

add_question("What is the max weight on the ramp toe in low?", "5,000 lbs")

def ask_questions():
    for question in question_list:
        print(question)
        print(option_letter[0] + "\n" + \
              option_letter[1] + "\n" + \
              option_letter[2] + "\n" + \
              option_letter[3])

print(ask_questions())