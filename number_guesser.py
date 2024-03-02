import random
top_of_range = input("type a number..:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print(f"You typed {top_of_range}. Please type a number greater than 0 next time.")
        quit()
else:
    print(f"You typed {top_of_range}. Please type a number next time.")
    quit()
        
random_number=random.randint(0,top_of_range)
# print(random_number)
comp_guess=[]
guesses=0
while True:
    guesses+=1
    # comp_guess.append(random_number)
    user_Guess=input('Make a guess.. ')
    if user_Guess.isdigit():
        user_Guess=int(user_Guess)
    else:
        print("Please type a number next time.")
        continue
    
    if(user_Guess==random_number):
        print("you got it.")
        break
    else:
        print("you got it wrong!")
        comp_guess.append(random_number)
        
print("You got it in ",guesses," guesses")
for n in comp_guess: 
    print(n)