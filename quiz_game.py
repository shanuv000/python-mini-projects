print("Welcome To My Computer Quiz")

playing = input("Do you want to play? ").lower()

if (playing != 'yes'):
    print('Game Closed. :(')
    quit()

print('Okay! Let\'s Play :)')
score = 0
answer = input('what does cpu stands for? ').lower()

if (answer == 'central processing unit'):
    score += 1
    print('Correct!')

else:
    print('Incorrect!!')

answer = input('What does GPU stands for ').lower()

if (answer == 'graphics processing unit'):
    score += 1
    print('Correct!')
else:
    print('Incorrect!!')

answer = input('What does RAM stands for? ').lower()

if (answer == 'random access memory'):
    score += 1
    print('Correct!')
else:
    print('Incorrect!!')

answer = input('What does PSU stands for? ').lower()

if (answer == 'power supply'):
    score += 1
    print('Correct!')
else:
    print('Incorrect!!')
print('You got'+str(score)+' questions correct.')
print('You got '+str((score/4)*100)+'%')
