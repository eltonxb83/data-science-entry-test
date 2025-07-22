'''Question 1/7 of pre-course assessment

   . Task 1:    To create a user defined function that would swap values of variables that are numerica
                when invoked and return -1 if "non-numeric" data type is detected.
     Task 2:    Invoke function "swap" using the following scenarios:
                 - "Apple", 10
                 - 9, 17

   . Date_16th July_25

   . Author: Elton Tay
'''
#Task 1 : defining swap function
def swap(x,y):
    #using 'if-else' and 'or' to check whether either variables is a str type 
    #and print result of "-1" if boolean results is true
    if type(x) == str or type(y) == str:        
        print("-1")                             
    else:
        #calling variables and assigning new values
        (x,y) = (y,x)
        # and printing out results 
        print(f"Swapped x value is now {x}")                             
        print(f"Swapped y value is now {y}")
    return

#Task 2 : Invoking the function swap
swap("Apple",10)
swap(9,17)