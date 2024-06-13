import random
# 1. The Range Riddle 

# Task 1:

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(days_of_week[::2])

# 3. Loop Condition Logic

# Task 2
player_xp = 0
player_lvl_up = "Congratulations! You've leveled up"
while player_xp < 5:
    print("1xp gained")
    player_xp += 1
    print(f"{5 - player_xp}xp to level up")
print(player_lvl_up)

# 4. Python's Random Game Night

# Task 1:

list_of_colors = ["red", "orange", "pink", "white", "black", "purple", "yellow", "blue", "green"]
random_color = random.choice(list_of_colors)
instructions = f"In this game a random color will be picked from the following list:\n{list_of_colors}\nYour job is to guess which color was selected. Good luck!"
print(instructions)
win = "You've guessed correctly, congrats!"
while True:
    player_guess = input("Make your guess:\n")
    if player_guess == random_color:
        print(win)
        break
    elif player_guess in list_of_colors:
        print("That's not the one! Try again")
    else:
        print("You've entered an invalid input")