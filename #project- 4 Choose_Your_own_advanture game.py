name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a road, it has come to end and you can go left ot right. Which way would you like to go? " ).lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? \n->Type walk to walk around and swim to swim accross: ")
    if answer == "swim":
        print("You swim across and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game." )
    else:
        print('Not a valid option. You lose.')
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    
    if answer == "back":
        print("You lose this advanture because you are going back. ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk with them (yes/no)? ")

        if answer == "yes":
            print("You talked to the stranger and they give you gold. You Won!!")

        elif answer == "no":
            print("you ignore the stranger and they are offended. You Lose the game!!")

        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose')
print("Thankyou for trying", name)