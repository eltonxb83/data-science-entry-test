'''Question 4/7 of pre-course assessment

   . Task 1:    To create a function that reveses a given string (s).
                s must be a string
                return the reversed string
     Task 2:    Invoke the function "string_reverse" using the following:
                "Hello World"
                Pyhton

   . Date_18th July_25

   . Author: Elton Tay
'''
#Task 1 : Defining string_reverse function
def string_reverse(s):
    #using if else statements to verify whether variable is string
    if not isinstance(s,str):
        #print response if variable is not string
        print(f'Variable is not a string.\n')
    else:
        #Using slicing (Start:end:step) and print function to perform reverse
        print(s[-1::-1])
    return

#Task 2 :Invoking string_reverse function
s = "Hello World"
string_reverse(s)

s = "Python"
string_reverse(s)
