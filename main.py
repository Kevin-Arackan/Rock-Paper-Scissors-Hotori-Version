rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

selection = [rock, paper, scissors]

print(("Welcome to Rock Papers Scissors vs Hotori!\n"
       "What do you choose?"))
player_choice_str = input("Select 0 for rock, 1 for paper, and 2 for scissors: ")
if not player_choice_str.isdigit() or int(player_choice_str) > 2 or int(player_choice_str) < 0:
    print("You ran away. You lose! Get whacked!")
    exit()

player_choice = int(player_choice_str)

# Precondition: player_choice is 0, 1, or 2
hotori_choice = player_choice + 1
if hotori_choice == len(selection):
    hotori_choice = 0

print(selection[player_choice])
print(f"Hotori chose: \n{selection[hotori_choice]}")

if player_choice == hotori_choice:
    print("It's a draw!")
# Scenarios where the player chooses the option right before the computer's choice in the list(all losing options)
elif player_choice + 1 == hotori_choice:
    print("You lose! Get whacked!")
else:
    # Accounting for the scenario where the player chooses scissors and the computer chooses rock
    if player_choice + 1 == hotori_choice + 3:
        print("You lose! Get whacked!")
    # In all other scenarios, the player wins
    else:
        print("You win!")
