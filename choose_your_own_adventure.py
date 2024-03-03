name = input('Type your name.')
print(f'Welcome {name} to this adventure')

answer = input(
    "You are at dirt road, It has come to an end and you can go left or right. Which way you would like to go? ").lower()

if answer == "left":
    answer = input(
        "You have come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across. ").lower()
    if answer == 'swim':
        print(
            f'{name} you swam across and got eaten by the elligator \nYou lost the game.')
    elif answer == 'walk':
        print(
            f"{name}, you walked for many miles, you got out of water \nYou lost the game.")
    else:
        print("Not a valid option you lose")
elif answer == "right":
    answer = input(
        f"{name}, you came to a bridge, it looks wobbly, Do you want to cross it or head back?\n(cross/back) ")
    if answer == 'back':
        print(f'{name} You back lose and lose')
    elif answer == 'cross':
        answer = input(
            'You cross the bridge and meet stranger. Will you talk to them?')
        if answer == 'yes':
            print(
                f"{name}, you talked to a stranger and theyh give you a gold and you win!! ")
        elif answer == "no":
            print("You ignored the stranger and they offended and you lose!!")
        else:
            print("Not a valid option you lose")

    else:
        print("Not a valid option you lose")
else:
    print("Not a valid option you lose")

print(f"thank you for trying, {name}")
