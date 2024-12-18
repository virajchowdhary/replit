import random
def infinite(Sides):
  print("")
  print("Infinity Dice")
  print("")
  sides=int(input("Hoe many sides does the dice have:"))
  N =random.randint(1,sides)
  print(N)
  T=input("Role Again?")
  if T.lower()=="yes":
    infinite(Sides)
  else:
    print("Thanks for playing")
infinite("Sides")