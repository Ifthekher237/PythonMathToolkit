# Try writing an “even-odd vending machine,” which will take a number as
# input and do two things:
# 1. Print whether the number is even or odd.
# 2. Display the number followed by the next 9 even or odd numbers.
# If the input is 2, the program should print even and then print 2, 4, 6,
# 8, 10, 12, 14, 16, 18, 20. Similarly, if the input is 1, the program should
# print odd and then print 1, 3, 5, 7, 9, 11, 13, 15, 17, 19.


def machine(n):
  if n%2==0:
    print("This is an EVEN number")
  else:
    print("This is an ODD number")

  #printing the number followed by the next 9 even or odd numbers.
  i=0
  while i<=9:
    print(n, end=" ")
    n+=2
    i+=1

  print()


n=float(input("Enter an integer: "))

if n.is_integer():
  n=int(n)
  machine(n)
else:
  print("Invalid input!")
