# times-table tester
import random

# functions improvement exercise
def timeTableDetails():
    timesTable = int(input("Enter the timestable you want to test: "))
    return timesTable
def generateQuestion(timesTable):
    for question in range (1,6):
        number1 = timesTable
        number2 = random.randrange(1,13)
        answer = number1 * number2
    return answer, number2
def formatQuestion(number1, number2):
    print("Question: {0}x{1}".format(number2,number1))
def finalAnswer(answer, number2):
    userAnswer = int(input(str(number2)+'x'+str(answer)+'= '))
    if userAnswer == answer:
        print("Answer correct")
        print()
    else:
        print("Answer incorrect")
        print()
def timesTableActual():
    timesTable = timeTableDetails()
    answer, number2 = generateQuestion(timesTable)
    question = formatQuestion(timesTable, number2)
    actualAnswer = finalAnswer(timesTable, number2)
    
#Main program
timesTableActual() 
