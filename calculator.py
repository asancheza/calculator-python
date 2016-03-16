#!/usr/bin/python
"""
Basic calculator written in python
"""

class Calculator: 
  def add (self, x, y):
    return x + y

  def substract (self, x, y):
    return x - y

  def multiply (self, x, y):
    return x * y

  def divide (self, x, y):
    return x / y

  def calculate (self, expr):
  	result = 0
  	operations = [ "+", "-", "*", "/" ]
  	expr = expr.replace(" ", "")
  	xchar = ""
  	ychar = ""
  	operation = None

  	for char in expr:
  		if char.isdigit():
  			if operation is None:
  				xchar = char
  			else:
  				ychar = char
  		else:
  			operation = char

  		if (ychar != ""):
  			if (operation == "*"):
  				result += self.multiply(int(xchar), int(ychar))

  			if (operation == "+"):
  				result += self.add(int(xchar), int(ychar))

  			if (operation == "/"):
  				result += self.divide(int(xchar), int(ychar))

  			if (operation == "-"):
  				result += self.substract(int(xchar), int(ychar))

  	return result
  	

calc = Calculator()
print calc.calculate("3 * 3 * 3")
print calc.calculate("3 - 3")
print calc.calculate("3 + 3")
print calc.calculate("3 * 2 * 4")
