import random
counter=0
print("Number from 1 to a Million guesser")
Answer=random.randint(1,1000000)
number = -1
if Answer<=1000000 and Answer>=1:
  print("Okay, let's start")
else:
  print("Not allowed restart program")
  exit()
while number != Answer:
  number=int(input("What is your guess:"))
  if number>1000000:
    print("That is not a valid number")
    print("Try again")
    continue
  elif number<1:
    print("Exiting program")
    exit()
  elif number<Answer and number>=1:
    print("Too low")
    print("Try again")
    counter+=1
    continue
  elif number>Answer and number<=1000000:
    print("To high")
    print("Try again")
    counter+=1
    continue 
  elif number==Answer:
    print("Correct")
    counter+=1
    break
  else:
    print("That is not valid")
    continue
print("It took you",counter,"guesse(s) to get it correct")