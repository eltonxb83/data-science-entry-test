'''Question 6/7 of pre-course assessment

   . Task 1:    To create a function that finds the first negative number in a list (lst)
                Return the first negative number if found, otherwise return "No negatives"
                Use a while loop to implement this.
     Task 2:    Invoke the function "find_first_negative" using the following scenario:
                [3, 5, -1, 7, -2, 8]
                [2, 10, 7, 0]

   . Date_19th July_25

   . Author: Elton Tay
'''
#Task 1: Defininf find_first_negative function
def find_first_negative(lst):
    #introducing "position maker" & assigning initial value of 1
    pos = 1
    #Creating a while loop where operation continues on while pos is less or equal
    #length of the lst
    while pos <= len(lst):
        #Creating and assigning the referenced number to temp_hold
        temp_hold = lst[pos-1]
        #Using if statement to verify whether temp_hold is negative
        if temp_hold < 0:
            #If statement is True, print value 
            print(temp_hold)
            #insert a return instead of break to prevent "no negative" statement from printing
            return
        else:
            #Moving position marker to the next at increment of 1
            pos += 1
    #Return "No Negatives" statement when while loop complete without any negative numbers found
    return print("No negatives")

#Task 2 : Invoking function
lst = [3,5,-1,7,-2,8]
find_first_negative(lst)

lst = [2,10,7,0]
find_first_negative(lst)