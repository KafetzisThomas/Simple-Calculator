#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Simple Calculator (https://github.com/KafetzisThomas/Simple-Calculator)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

class Calculator:
  """Model a calculator"""
  def __init__(self, first_number, second_number):
    """Initialize the user input attributes"""
    self.first_number = first_number
    self.second_number = second_number

  def addition(self):
    """Print a statement about adding two values"""
    print(self.first_number + self.second_number)

  def subtraction(self):
    """Print a statement about subtracting two values"""
    print(self.first_number - self.second_number)
  
  def multiplication(self):
    """Print a statement about multiplying two values"""
    print(self.first_number * self.second_number)

  def division(self):
    """Print a statement about dividing two values"""
    print(self.first_number / self.second_number)

first_number = float(input("\nWrite first number: "))
second_number = float(input("Write second number: "))

c = Calculator(first_number, second_number)
print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = str(input("\nChoice (1-4): "))

if choice == "1": c.addition()
elif choice == "2": c.subtraction()
elif choice == "3": c.multiplication()
elif choice == "4": c.division()
else: print("Undefined choice.")
