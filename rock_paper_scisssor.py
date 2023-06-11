import random

options=["rock","paper","scissor"]
user_wins=0
com_wins=0

while True:
    user_input=input("Type Rock/Paper/Scissor or Q to Quit:").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    #rock:1,paper:1,scissor:2
    com_pick=options[random_number]
    print("Computer picked:",com_pick)

    if user_input=="rock" and com_pick=="scissor":
        print("User won!!")
        user_wins+=1
        continue
    elif user_input=="paper" and com_pick=="rock":
        print("User won!!")
        user_wins+=1
        continue
    elif user_input=="scissor" and com_pick=="paper":
        print("User won!!")
        user_wins+=1
        continue
    elif user_input=="rock" and com_pick=="rock":
        print("**************Redo the game***************")
        continue
    elif user_input=="paper" and com_pick=="paper":
        print("**************Redo the game***************")
        continue
    elif user_input=="scissor" and com_pick=="scissor":
        print("**************Redo the game***************")
        continue
    else:
        print("User lost!!")
        com_wins+=1
    
print("User won ",user_wins," times.")
print("Computer won ",com_wins," times.")
print("GoodBye!!")    