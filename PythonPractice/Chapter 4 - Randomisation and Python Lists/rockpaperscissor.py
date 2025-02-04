import random

choice = ["rock", "paper", "scissors"]
pc_choice = random.choice(choice)
player_choice = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n")
print("You chose: " + player_choice)
print("Computer chose: " + pc_choice)

if player_choice == "0":
    if pc_choice == choice[0]:
        print("draw.")
    elif pc_choice == choice[1]:
        print("lose")
    else:
        print("win")
elif player_choice == "1":
    if pc_choice == choice[1]:
        print("draw.")
    elif pc_choice == choice[2]:
        print("lose")
    else:
        print("win")
elif player_choice == "2":
    if pc_choice == choice[2]:
        print("draw.")
    elif pc_choice == choice[0]:
        print("lose")
    else:
        print("win")
else:
    print("invalid. lose")
