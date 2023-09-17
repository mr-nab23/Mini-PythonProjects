name = input("Type your name : ")
print("Welcome",name,"to this adventure!")
answer= input("You are on a secret path with knowhere to be found , it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? ")
    if answer=="swim":
        print("You swam across and were eaten by crocodiles")
    elif answer=="walk":
        print("You walked for too long, ran out of supplies and DIE")
    else:
        print('Wrong decision--DIE--')


elif answer =="right":
    answer=input("You found a bridge , it looks wobbly , do you want to cross it or head back? (cross/back)")

    if answer=="back":
        print("You went back and DIE because there were bears waiting")
    elif answer=="cross":
        print("You crossed the bridge and meet a strange looking guy . Do you talk to him(yes/no)? ")
        
        if answer =="yes":
            print("You talk to the stranger and he shoots you .DIE ")
        elif answer == "no":
            print("You ignore the stranger and keep walking until you found a small village. You WIN =)")
        else:
            print('Wrong decision--DIE--')
    else:
        print('Wrong decision--DIE--')
else:
    print('Wrong decision--DIE--')