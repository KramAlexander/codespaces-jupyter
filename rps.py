import random
input = input("Please choose: rock, paper, scissor")
choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)

# equal
if input == computer:
    print("You chose the same option as the computer did:" + input)
# not equal, player wins
elif input == "rock" and computer == "scissor":
    print("You win with rock against scissor")
elif input == "paper" and computer == "rock":
    print("You win with paper against rock")
elif input == "scissor" and computer == "paper":
    print("You win with scissor against paper")
# not equal, computer wins
elif input == "rock" and computer == "paper":
    print("You lose with rock against paper")
elif input == "paper" and computer == "scissor":
    print("You lose with paper against scissor")
elif input == "scissor" and computer == "rock":
    print("You lose with scissor against rock")