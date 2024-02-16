"""
Take the input from user and find out the area of square
"""


def square_area(length, breadth):
    area_of_square = round((length * breadth), 4)

    return area_of_square


length = float(input("Please enter the length of square: "))
breadth = float(input("Please enter the breadth of square: "))

x = square_area(length, breadth)
print(f"Are of square is : {x}")
