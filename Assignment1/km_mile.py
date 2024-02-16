"""
python program to convert kilometer to mile. ASk  kilometer from User.

"""


def kilometer_mile(km):

    distance_kilometer = int(km)
    distance_in_mile = round(distance_kilometer * 0.621371, 2)
    return distance_in_mile


user_input = input(
    "Please enter the distnce in KM that you want to be converted in miles: "
)
print(f"Distnce in miles: {kilometer_mile(user_input)}")
