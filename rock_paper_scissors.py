import random

user_wins = 0
compute_wis = 0
options = ["rock","paper","scissors"]
while True:
    user_input = input("Choss Rock/Paper/Scissors or Q to quit the game. ").lower()
    if user_input =='q':
        break
    if user_input not in options:
        print('Please check the valid Option:')
        continue
    
    random_number=random.randint(0,2)
    # rock is 0, paper is 1, scissors is 2
    computer_pick = options[random_number]
    print('Compuer picked',computer_pick)
print("GoodBye")