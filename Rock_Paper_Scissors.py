import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper" , "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input =="q":
        break
    
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    #rock:0, paper:1, scissors:2
    computer_picks = options[random_number]
    print("Computer picked ",computer_picks + ".")

    if user_input =="rock" and computer_picks =="scissors":
        print("You won! ")
        user_wins +=1
        continue

    elif user_input =="paper" and computer_picks =="rock":
        print("You won! ")
        user_wins +=1
        continue

    elif user_input =="scissors" and computer_picks =="paper":
        print("You won! ")
        user_wins +=1
        continue
    else:
        print("You lost!")
        computer_wins += 1
        continue

print("You've won " ,user_wins,"times")
print ("The computer won" ,computer_wins,"times.")
print("Goodbye")



