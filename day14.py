from getpass import getpass as input
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print("Select your move (R, P or S)")
Player1 = input("Player 1 > ")
Player2=input("Player 2 > ")
if Player1 == "R" and Player2 == "P":
    print("Players one Rock Loses to Players two Paper")
elif Player1 == "R" and Player2 == "S":
    print("Players one Rock Wins to Players two Scissors")
elif Player1 == "R" and Player2 == "R":
  print("Players one Rock Ties to Players two Rock try again")
elif Player1 == "P" and Player2 == "R":
  print("Players one Paper Wins to Players two Rock")
elif Player1 == "P" and Player2 == "S":
  print("Players one Paper Loses to Players two Scissors")
elif Player1 == "P" and Player2 == "P":
  print("Players one Paper Ties to Players two Paper try again")
elif Player1=="S" and Player2=="R":
  print("Players one Scissors Loses to Players two Rock")
elif Player1=="S" and Player2=="P":
  print("Players one Scissors Wins to Player two Paper")
elif Player1=="S" and Player2=="S":
  print("Players one Scissors Ties to Players two Scissors try again")
else:
  print("TYPE UPPER CASE R, P, S")