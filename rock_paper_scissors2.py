import random
randoms=random.randint(0,2)
options = ["rock","paper","scissors"]
while True:
    
    player_guessed = input('Enter the rock,paper or scissors =>  ')
    if player_guessed =='q':
        break
    computer_guessed=options[randoms]
    print(f"You chose {player_guessed} and computer guessed {computer_guessed}")
    if player_guessed == 'rock' and computer_guessed=='scissors':
        print('you win')
    elif player_guessed =='paper' and computer_guessed=='rock':
         print('You win')
    elif player_guessed=='scissors' and computer_guessed=='paper':
        print('You win')
    elif player_guessed == computer_guessed:
        print('Its a tie')
    else :
      print('Computer wins')
        
print("Game Over")