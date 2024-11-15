# math test that generates random math questions for practice and doesn't let the user continue until they get it correct
# addition, subtraction, multiplication, division, exponent

import random #to randomly generate operands
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 0
MAX_OPERAND = 12
TOTAL_QUES = 10

def generate_math():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression, answer

wrong = 0
input("Press enter to start!")
print("---------------------")

timer_start = time.time()

for i in range(TOTAL_QUES):
    expression, answer = generate_math()
    while True:
        guess = input("Question #" + str(i+1) + ": " + expression + " = ")
        if guess == str(answer):
            break
        wrong += 1

timer_end = time.time()
timer_total = round(timer_end - timer_start, 2)

print("---------------------")
print("You have successfully completed the assessment!")
print("You took " , timer_total , "seconds!")
