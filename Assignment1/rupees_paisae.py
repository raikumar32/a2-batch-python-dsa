"""
ask user input in ruppes and conver it to paisae
"""


def rupee_to_pisae(rupees):
    paise = int(rupees) * 100
    return paise


rupees = input("Please enter the ruppe that want to be converted ")
x = rupee_to_pisae(rupees)
print(f"currency in paisae: {x}")
