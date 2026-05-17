a = input("Enter your choice (rock/paper/scissors): ")
b = input("Enter your choice (rock/paper/scissors): ")
if a == b:
    print("It's a tie!")
elif (a == 'rock' and b == 'scissors') or (a == 'paper' and b == 'rock') or (a == 'scissors' and b == 'paper'):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")