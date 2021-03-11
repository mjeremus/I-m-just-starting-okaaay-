from random import randint

player_wins = 0
cp_wins = 0

while player_wins < 3 and cp_wins < 3:
    print(f"Player score: {player_wins} | Computer score: {cp_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input("Player, make your move: ").lower()
    
    if player == "exit" or player == "q" or player == "quit":
        break
        
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}")

    if player == "rock" and computer == "paper":
        print("Computer wins")
        cp_wins += 1
    elif player == "paper" and computer == "rock":
        print("Player wins")
        player_wins += 1
    elif player == "rock" and computer == "scissors":
        print("Player wins")
        player_wins += 1
    elif player == "scissors" and computer == "rock":
        print("Computer wins")
        cp_wins += 1
    elif player == "paper" and computer == "scissors":
        print("Computer wins")
        cp_wins += 1
    elif player == "scissors" and computer == "paper":
        print("Player wins")
        player_wins += 1
    else:
        print("It's a draw")
        
if player_wins > cp_wins:
    print("YOU WON! CONGRATS")
elif player_wins < cp_wins:
    print("NOT THIS TIME :( SORRY")
else:
    print("T.HANKS")
print(f"FINAL SCORE! \nPLAYER: {player_wins} | COMPUTER: {cp_wins}")