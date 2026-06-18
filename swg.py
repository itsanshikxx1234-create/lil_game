import random
choices=["snake","water","gun"]
while True:
    user_input=input("Enter your choice (snake,water or gun):")
    if user_input not in choices:
        print("invalid choice, please try again.")
        continue
    computer_choice=random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    print(f"you chose:{user_input}")
    if user_input==computer_choice:
        print("It's a tie!")
    elif (user_input=="snake"and computer_choice=="water") or (user_input=="water" and computer_choice=="gun") or (user_input=="gun" and computer_choice=="snake"):
        print("You Win!")
    else:
        print("Computer Wins!")
