import random
def rollDice(sides):
  N =random.randint(1,sides)
  return N
def roll_6_and_12():
  roll_6_sided_dice = rollDice(6)
  roll_12_sided_dice = rollDice(12)
  health = ((roll_6_sided_dice * roll_12_sided_dice)/2)+10
  return health
def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  strength = ((roll_6_sided_dice * roll_8_sided_dice)/2)+12
  return strength

print("⚔️Character Builder⚔️")
haveACharacter = "yes"
while haveACharacter == "yes":
  Name=input("Name your legend:")
  Type=input("Character type(Human,Elf,Wizard,Orc):")
  print(Name)
  health = roll_6_and_12()
  print("Health:",health,)
  strength = roll_6_and_8()
  print("Strength:", strength)
  print("May your name go down in Legend...")
  haveACharacter = input("Want to try again")
  if haveACharacter.lower()=="no":
   break
os.system("clear")