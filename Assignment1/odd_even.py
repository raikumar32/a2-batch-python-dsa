"""
Ask a number from user. Print if the number is ODD or EVEN.
"""


def odd_even(number):
    if number % 2 == 0:
        return " Number is Even"
    else:
        return " Number id odd"


x = int(input("Please enter the number you want to check: "))

y = odd_even(x)
print(f"{y}")
