import random

while True:
    my_choice = input("Choose: rock, paper or scissors: ")
    my_choice = my_choice .lower()

    if my_choice == "quit":
        break

    if my_choice != "rock" and my_choice != "paper" and my_choice != "scissors":
        print("Please choose a correct answer")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice }")

    if my_choice  == computer_choice :
        print("You tied")
        
    elif my_choice == "paper" and computer_choice  == "rock":
        print("YOU Win!")
        break
    
    elif my_choice == "rock" and computer_choice  == "scissors":
        print("YOU Win!")
        break
    
    elif my_choice == "scissors" and computer_choice  == "paper":
        print("YOU Win!")
        break
    
    else:
        print("You lose. Try again!")
