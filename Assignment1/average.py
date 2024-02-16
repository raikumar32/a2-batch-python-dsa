"""
Ask 3 numbers from users and calculate the average
"""


def avg_number(user_input_list):

    avg_output = round((sum(user_input_list) / len(user_input_list)), 2)

    return avg_output


number = [int(x) for x in input("please enter your number comma seprated:").split(",")]
print(number)
x = avg_number(number)
print(f"avg of the numbers:{x}")
