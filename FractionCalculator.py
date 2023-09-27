from fractions import Fraction


def add(a,b):
  print('Result of Addition: {0}'.format(a+b))


def subtract(a,b):
  print('Result of Subtraction: {0}'.format(a-b))


def multiply(a,b):
  print('Result of Multiplication: {0}'.format(a*b))


def divide(a,b):
  print('Result of Division: {0}'.format(a/b))



a=Fraction(input("Enter first fraction: "))
b=Fraction(input("Enter second fraction: "))

op = input('Operation to perform - ADD, SUBTRACT, DIVIDE, MULTIPLY: ')

if op.upper()=="ADD":
  add(a,b)
elif op.upper()=="SUBTRACT":
  subtract(a,b)
elif op.upper()=="MULTIPLY":
  multiply(a,b)
elif op.upper()=="DIVIDE":
  divide(a,b)
