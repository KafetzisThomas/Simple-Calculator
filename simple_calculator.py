#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Simple Calculator (https://github.com/KafetzisThomas/Simple-Calculator)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def addition(self):
        print(self.x + self.y)
    
    def subtraction(self):
        print(self.x - self.y)
    
    def multiplication(self):
        print(self.x * self.y)
    
    def division(self):
        print(self.x / self.y)

a = float(input("\nWrite the first number: "))
b = float(input("Write the second number: "))

c = Calculator(a,b)
print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = str(input("\nChoice (1-4): "))

if(choice=="1"):
    c.addition()
elif(choice=="2"):
    c.subtraction()
elif(choice=="3"):
    c.multiplication()
elif(choice=="4"):
    c.division()
else:
    print("Undefined choice.")
