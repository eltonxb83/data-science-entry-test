'''Question 7/7 of pre-course assessment

   . Task 1:    To define a class named Car with attributes: make, model, year
                Initialize these attributes in the __init__ mehtod
                Add a method named describe_car() that prints information abouve the car as
                "Year Make Model"
     Task 2:    Create an instance of the Car class with the following attributes and call
                describe_car method:
                -Make: Toyota, Model: Corolla, Year: 2020  

   . Date_20th July_25

   . Author: Elton Tay
'''
#Defining Car class with self, make, model, year attributes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    #defining describe_car function that prints car informatiom
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

#Task 2: Creating an instance of Car class and invoking describe_car function
car_1 = Car("Toyota", "Corolla", "2020")
car_1.describe_car()