'''Question 3/7 of pre-course assessment

   . Task 1:    To create a function that updates a dictionary (dct) with a new key-value pair.
                If the key already exist in dct, print the original valuem then update its valye.
                Return the updated dictionary
     Task 2:    Invoke the function "update_dictionary" using the following scenarios:
                - {}, "name", "Alice"
                -{"age" : 25}, "age", 26

   . Date_18th July_25

   . Author: Elton Tay
'''
#Task 1 : Definging update_dictionary function
def update_dictionary(dct,key,value):
    #Using if statements to verify whether key already exist in the dct
    if key in dct.keys():
        #Printing statement showinging original value before updating 
        print(f'Original value of "{key}" is {dct[key]}.')
    #Assigning new value 
    dct[key] = value
    return 

#Task 2 : Invoking update_dictionary function
dct = {}
update_dictionary(dct,"name","Alice")
print(dct)

dct = {"age":25}
update_dictionary(dct,"age","26")
print(dct)