# times-table tester
import random

# functions improvement exercise
def timeTableDetails():
    timesTable = int(input("Enter the timestable you want to test: "))
    return timesTable
def generateQuestions(timesTable, questions):
    for questions in range (1,6):
        number1 = timesTable
        number2 = random.randrange(1,13)
        answer = number1 * number2
    print("Question: {0} ".format(questions))
    return answer
def finalAnswer(userAnswer, answer):
    userAnswer = int(input(str(number1)+'x'+str(number2)+'=?'))
    if userAnswer == answer:
        print("Answer correct")
        print()
    else:
        print("Answer incorrect")
        print()
def timesTableActual():
    timesTable = timeTableDetails()
    questions = generateQuestions(timesTable, questions)

#Main program
timesTableActual()
