# times-table tester
import random

# functions improvement exercise
def timeTableDetails():
    timesTable = int(input("Enter the timestable you want to test: "))
    return timesTable
def generateQuestions(timesTables, questions):
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
    questions = generateQuestions(timesTable


# main program
#print("Times-table tester")
#print()
#testTable = input("Which times-table do you want to be tested on? ")
#testTable = int(testTable)
#for questions in range(1,6):
    #Num1 = testTable
    #Num2 = random.randrange(2,13)
    #Ans = Num1 * Num2
    #UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
    #UserAnswer = int(UserAnswer)
    #if UserAnswer == Ans:
        #print('Well done, you got the correct answer!')
        #print()
    #else:
        #print('Sorry, you got the answer wrong. The correct answer is',Ans)
        #print()
              
