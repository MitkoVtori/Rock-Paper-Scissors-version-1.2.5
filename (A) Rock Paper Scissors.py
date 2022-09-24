from random import randint
from time import sleep

# We have this list so for example, the player chose: r, R, Rock, rock, ROCK, RoCk, rOck & others it will still be rock
rock = ["R", "r"]
paper = ["P", "p"]
scissors = ["S", "s"]
# We're using the a, b, c for the random randint
a = "rock"
b = "paper"
c = "scissors"

print("Choose between Rock, Paper and Scissors")
player = input()
# here we check if R, r, P, p or S, s is the first letter
if rock[0] in player[0] or rock[1] in player[0]:
    player = "rock"
elif paper[0] in player[0] or paper[1] in player[0]:
    player = "paper"
elif scissors[0] in player[0] or scissors[1] in player[0]:
    player = "scissors"
else:
    print(f"{player} is not a valid command!")
    print("I'll choose!")
    player = randint(1, 3)
    if player == 1:
        player = "rock"
    elif player == 2:
        player = "paper"
    else:
        player = "scissors"
    # The command sleep() tells the program how much time to wait before printing. (works in seconds)
    sleep(1)
    print("____________________")
    sleep(1)
    print("....................")
    sleep(0.5)
    print(f'''"{player}"''')

computer = randint(1, 3)
if computer == 1:
    computer = "rock"
elif computer == 2:
    computer = "paper"
else:
    computer = "scissors"
print()
sleep(0.10)
print("rock")
sleep(0.20)
print("paper")
sleep(0.30)
print('Scissors')
sleep(0.30)
print("Shoot!")
print()
sleep(0.1)
print(f"You chose \"{player}\" and the computer chose \"{computer}\"")
if (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
    sleep(0.2)
    print("You win!")
elif player == computer:
    sleep(0.2)
    print("You're Draw!")
else:
    sleep(0.3)
    print("You lose!")