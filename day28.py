import random,os,time
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

while True:
  print("⚔️Character Builder⚔️")
  NameA=input("Name your legend:")
  TypeA=input("Character type(Human,Elf,Wizard,Orc):")
  print(NameA)
  healthA = roll_6_and_12()
  print("Health:",healthA,)
  strengthA = roll_6_and_8()
  print("Strength:", strengthA)
  print("May your name go down in Legend...")
  print("Who are they battling?")
  time.sleep(1)
  os.system("clear")
  break
while True:
  print("⚔️Character Builder⚔️")
  NameB=input("Name your legend:")
  TypeB=input("Character type(Human,Elf,Wizard,Orc):")
  print(NameA)
  healthB = roll_6_and_12()
  print("Health:",healthB,)
  strengthB = roll_6_and_8()
  print("Strength:", strengthB)
  print("May your name go down in Legend...")
  print("Who are they battling?")
  time.sleep(1)
  os.system("clear")
  break
counter=1
winner=None
while True:
  time.sleep(2)
  os.system("clear")
  print("⚔️Battle Time⚔️")
  print()
  print("The battle begins!")



  PT1=rollDice(6)
  PT2=rollDice(6)

  diffrence=abs(strengthA-strengthB)+1
  
  if PT1>PT2:
    healthB -=diffrence
    if counter==1:
     print(NameA,"wins the first blow")
    else:
      print(NameA,"wins round",counter)
  if PT2>PT1:
    healthA -=diffrence
    if counter==1:
     print(NameB,"wins the first blow")
    else:
      print(NameB,"wins round",counter)
  elif PT1==PT2:
    print("Their swords clash and they draw round",counter)
    
  print()
  print(NameA)
  print("Health:",healthA,)
  print(NameB)
  print("Health:",healthB,)
  if healthA<=0:
    print(NameA,"Has Lost")
    winner=NameB
    break
  elif healthB<=0:
    print(NameB,"Has Lost")
    winner=NameA
    break
  else:
    print("And they're both standing for the next round")
    counter+=1
  if healthA<=0 or healthB<=0:
    time.sleep(1)
    os.system("clear")
    print("⚔️Battle Time⚔️")
    print()
    print("The battle begins!")
    print(winner,"Has Won In",counter,"rounds")