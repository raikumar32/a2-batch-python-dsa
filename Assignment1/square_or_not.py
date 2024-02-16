"""
Take values of length and breadth of a rectangle from user and check if it is square or not.

"""

length = int(input("Please enter the length : "))
breadth = int(input("please enter the breadth: "))

if length == breadth:
    print("This is square")
else:
    print("This is not a square")
