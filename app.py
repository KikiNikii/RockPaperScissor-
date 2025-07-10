#Starting questions - two players
player1 = input("Get ready to play rock paper scissors! PICK ONE, NO PEEEKING ") 
player2 = input("Get ready to play rock paper scissors! PICK ONE, NO PEEKING ")

#Ties
if player1 == player2:
    print("You both got " + player1)

#Picking Winners
if player1 == "rock":
    if player2 == "paper":
        print("Player 2 Wins!")
    elif player2 == "scissors":
        print("Player 1 Wins!")

if player1 == "paper":
    if player2 == "rock":
        print("Player 1 Wins!")
    elif player2 == "scissors":
        print("Player 2 Wins!")

if player1 == "scissors":
    if player2 == "rock":
        print("Player 2  Wins!")
    elif player2 == "paper":
        print("Player 1 Wins!")

# if x == 5:
#     if y == 6:
#         print("true")
#     elif z == 8:
#         print("fun")
