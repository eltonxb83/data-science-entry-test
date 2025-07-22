'''Question 5/7 of pre-course assessment

   . Task 1:    To create a function to check if the number (num) is divisible by another number (divisor)
                Both num and divisor must be numeric
                Return True if num is divisible by divisor, False otherwise
     Task 2:    Invoke the function "check_divisibility" using the following scenarios:
                10, 2
                7, 3

   . Date_18th July_25

   . Author: Elton Tay
'''
#Task 1: Defining function
def check_divisibility(num,divisor):
    #using if else statments and isinstance function to determine whether input is numberic
    if isinstance(num,str)  or isinstance(divisor,str):
        #Print statement when non-numberic variable is detected
        print("Variables must not be string type.")
    else:
       #using % arithematic operator and == to determine dividisibility
       #with True if divisible and False if there is remainder
       return print(num%divisor == 0)
    
#Task 2: Invoking function
num = 10
divisor = 2
check_divisibility(num,divisor)

num = 7
divisor = 3
check_divisibility(num,divisor)
    