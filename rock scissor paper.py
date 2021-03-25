
import random
user_action=input("enter choice")
computer_action=random.choice(["rock","scissors", "paper"])
print(" you",user_action)
print("computer",computer_action)
if user_action ==computer_action:
    print ("its tie")
elif user_action=="rock":
    if computer_action=="scissor":
        print('rock smashes scissor, you win!')
    else:
        print("paper covers rock!you lose.")
elif user_action=="scissor":
    if  computer_action=="paper":
        print(' scissor cut paper! you win!')
    else:
        print("rock smashes scissor !you lose.")
elif user_action=="paper":
    if computer_action=="rock":
        print('paper covers rock, you win!')
    else:
        print("scissor cut paper !you lose.")


      