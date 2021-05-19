### a quiz app for SKT
import random

question_list = []
answer_list = []
option_letter = ["A. ", "B. ", "C. ", "D. "]
answer_options = []

def add_question(question, answer, a1, a2, a3):
    question_list.append(question)
    answer_list.append(answer)
    answer_options.append([a1, a2, a3])

add_question("What is the max weight on the ramp toe in low?", "5,000 lbs", "8,500 lbs", "9,100 lbs", "10,355 lbs")
add_question("What is the max load on a bi-directional roller?", "2,000 lbs", "1,500 lbs", "1,940 lbs", "1,000 lbs")



def ask_questions():
    points = 0
    i = 0
    for question in question_list:
        x = random.randint(1, 4)
        print(question)
        if x == 1:
            print(option_letter[0] + answer_list[i] + "\n" +\
                option_letter[1] + answer_options[i][0] + "\n" +\
                option_letter[2] + answer_options[i][1] + "\n" +\
                option_letter[3] + answer_options[i][2])
            input_answer = input("Answer: ")
            if input_answer == "A." or input_answer == "A":
                points += 1
            else:
                points += 0
        elif x == 2:
            print(option_letter[0] + answer_options[i][0] + "\n" +\
                  option_letter[1] + answer_list[i] + "\n" +\
                  option_letter[2] + answer_options[i][1] + "\n" +\
                  option_letter[3] + answer_options[i][2])
            input_answer = input("Answer: ")
            if input_answer == "B." or input_answer == "B":
                points += 1
            else:
                points += 0
        elif x == 3:
            print(option_letter[0] + answer_options[i][0] + "\n" +\
                  option_letter[1] + answer_options[i][1] + "\n" +\
                  option_letter[2] + answer_list[i] + "\n" +\
                  option_letter[3] + answer_options[i][2])
            input_answer = input("Answer: ")
            if input_answer == "C." or input_answer == "C":
                points += 1
            else:
                points += 0
        else:
            print(option_letter[0] + answer_options[i][0] + "\n" +\
                  option_letter[1] + answer_options[i][1] + "\n" +\
                  option_letter[2] + answer_options[i][2] + "\n" +\
                  option_letter[3] + answer_list[i])
            input_answer = input("Answer: ")
            if input_answer == "D." or input_answer == "D":
                points += 1
            else:
                points += 0
        i += 1
    score = points / len(question_list) * 100
    return ("Your Score: " + str(score) + "%")



print(ask_questions())
