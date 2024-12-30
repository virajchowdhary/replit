sentence = input("Enter a sentence to get rainbow slicing: ")
def ColorChange(color):
  if color=="r":
      print("\033[31m", end="")
  elif color==" ":
      print("\033[0m", end="")
  elif color=="b":
      print("\033[34m", end="")
  elif color=="y":
      print("\033[33m", end="")
  elif color == "g":
      print("\033[32m", end="")
  elif color == "p":
      print("\033[35m", end="")
print()
for letter in sentence:
  ColorChange(letter.lower())
  print(letter, end="")
  