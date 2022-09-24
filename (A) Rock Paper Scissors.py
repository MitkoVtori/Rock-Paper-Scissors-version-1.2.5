from random import randint
from time import sleep

# We have this list so for example, the player chose: r, R, Rock, rock, ROCK, RoCk, rOck & others it will still be rock
rock = ["R", "r"]
paper = ["P", "p"]
scissors = ["S", "s"]
# Creating this flag so we can stop the while loop
stop_playing = False
# We're using the a, b, c for the random randint
a = "rock"
b = "paper"
c = "scissors"
# If the player wants to see his statistics
stats = "stats"

# statistics
win = 0
lose = 0
draw = 0
# how many times the player have chosen rock, paper or scissors
player_rock = 0
player_paper = 0
player_scissors = 0
# how many times the computer have chosen rock, paper or scissors
computer_rock = 0
computer_paper = 0
computer_scissors = 0
while not stop_playing:
    print("Choose between Rock, Paper and Scissors")
    player = input()
    # here we check if R, r, P, p or S, s is the first letter
    if rock[0] in player[0] or rock[1] in player[0]:
        player_rock += 1
        player = "rock"
    elif paper[0] in player[0] or paper[1] in player[0]:
        player_paper += 1
        player = "paper"
    elif scissors[0] in player[0] or scissors[1] in player[0]:
        player_scissors += 1
        player = "scissors"
    else:
        print(f"{player} is not a valid command!")
        print("I'll choose!")
        player = randint(1, 3)  # randint() chooses a random number between a and b
        # We change the number with a string
        if player == 1:
            player_rock += 1
            player = "rock"
        elif player == 2:
            player_paper += 1
            player = "paper"
        else:
            player_scissors += 1
            player = "scissors"
        # The command sleep(seconds) stops the program for the writen amount.
        sleep(1)
        print("____________________")
        sleep(1)
        print("....................")
        sleep(0.5)
        print(f'''"{player}"''')

    computer = randint(1, 3)
    if computer == 1:
        computer_rock += 1
        computer = "rock"
    elif computer == 2:
        computer_paper += 1
        computer = "paper"
    else:
        computer_scissors += 1
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
        win += 1
    elif player == computer:
        sleep(0.2)
        print("You're Draw!")
        draw += 1
    else:
        sleep(0.3)
        print("You lose!")
        lose += 1

    print("Do you want to play another game? Type (y) for Yes and (n) for no")
    another_game = input()
    if another_game[0] == "y" or another_game[0] == "Y":
        # We check if the player wants to see his statistics
        print("type \"stats\" to see your statistics, type anything else to continue")
        see_statistics = input()
        if see_statistics == stats or see_statistics == stats.upper:
            sleep(0.5)
            print(f"Wins: {win}")
            sleep(0.5)
            print(f"Draws: {draw}")
            sleep(0.5)
            print(f"Loses: {lose}")
        continue
    else:
        stop_playing = True

print(f'''
Wins: {win}
Draws: {draw}
Loses: {lose}
''')
sleep(0.5)
print(f"You have chosen Rock {player_rock} times, Paper {player_paper} times and Scissors {player_scissors} times.")
sleep(0.3)
print(f"Computer have chosen Rock {computer_rock} times, Paper {computer_paper} times and Scissors {computer_scissors} "
      f"times.")
print()
sleep(0.2)
print("BYEE!!!")