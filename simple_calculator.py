#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Simple Calculator (https://github.com/KafetzisThomas/Simple-Calculator)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

def calculate():
    a = float(input("Write the first number: "))
    b = float(input("Write the second number: "))
    c = str(input("Write the symbol: "))

    if c == "+":
        d = a + b
        print("Resault: {}".format(d))
    elif c == "-":
        d = a - b
        print("Resault: {}".format(d))
    elif c == "*":
        d = a * b
        print("Resault: {}".format(d))
    elif c == "/":
        d = a / b
        print("Resault: {}".format(d))
    else:
        print("Undefined symbol. Try Again!")
        calculate()

calculate()