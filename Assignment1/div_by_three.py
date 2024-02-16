"""
Q7. Check if the number entered by User is divisible by 3 or not
"""


def div_by_three(number):
    if int(number) % 3 == 0:
        return "number is divisibale by 3"
    else:
        return "number is not divisiable by 3"


user_input = input("Please enter that you want to check : ")
x = div_by_three(user_input)
print(f"{x}")
