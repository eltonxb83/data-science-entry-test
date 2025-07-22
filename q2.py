'''Question 2/7 of pre-course assessment

   . Task 1:    To create a function that searches for all ocurrences of a value (find_val) in a given list (lst)
                and replaces them with another value (replace_val).
                Lst must be a list.
                Return the modified list.
     Task 2:    Invoke the function "find_and_replace" using the following scenarios:
                - [1, 2, 3, 4, 2, 2], 2, 5
                -["apple", "banana", "apple"], "apple" , "orange"

   . Date_16th July_25

   . Author: Elton Tay
'''
#Task 1: defining find_and_replace function
def find_and_replace(lst, find_val, replace_val):
    #creating an empty list named "modified_list"
    modified_lst = []
    #using a 'for' , 'elseif' statements and append() function to
    #find and replace values
    for char in lst:
        if char != find_val:
           modified_lst.append(char)
        else:
           modified_lst.append(replace_val)
    return print(modified_lst)

#Task 2: Invokgin defined function
lst=[1,2,3,4,2,2]
find_val = 2
replace_val = 5
find_and_replace(lst,find_val,replace_val)

lst=["apple","banana","apple"]
find_val = "apple"
replace_val = "orange"
find_and_replace(lst,find_val,replace_val)