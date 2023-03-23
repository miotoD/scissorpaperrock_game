print("~~~~Welcome to rock paper scissor arcade!~~~~")
import random
playerone = input("Choose a pick! (rock/paper/scissor): ")
options = ["rock", "paper", "scissor"]
AI = random.choice(options)
print("The AI chose: " + AI)

if playerone == "rock" and AI == "paper":
    print("Paper beats rock! You lose.")
elif playerone == "rock" and AI == "scissor":
    print("Rock beats scissor! You win.")
elif playerone == "paper" and AI == "rock":
    print("Paper beats rock! You win.")
elif playerone == "paper" and AI == "scissor":
    print("Scissor beats paper! You lose.")
elif playerone == "scissor" and AI == "rock":
    print("Rock beats scissor! You lose.")
elif playerone == "scissor" and AI == "paper":
    print("Scissor beats paper! You win.")
else:
    print("It's a tie!")