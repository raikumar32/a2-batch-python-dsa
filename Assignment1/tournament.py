"""
Ask number of games played in a tournament. 
Ask the user number of games won and number of games loss. 
Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)


"""

total_number_of_games = int(input("Please enter the number of games you have played: "))
number_of_games_won = int(input("Please enter the number of games you have won : "))
number_of_games_lost = int(input("Please enter the number of games you have lost: "))
number_of_games_tie = total_number_of_games - (
    number_of_games_won + number_of_games_lost
)

points_won = (number_of_games_won * 4) + (number_of_games_tie * 2)

print(f"Number of points in won: {points_won}")
