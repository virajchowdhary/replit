print("Welcome to good or bad generator")
print("")
Think=input("Do you want to feel good or bad today: ")
name=input("What is your name: ")
Achieve=input("What do you want to achieve: ")
Scale=input("On a scale of 1 to 10 how do you feel today: ")
print("")
if Think.lower() == "good":
  print("Hello",name,"you are a good person")
  print("You are going to",Achieve,"today")
  print("Remember you are a shining star that will outshine everyone")
  print("Everyone wants to be like you")
  print("Even though you feel like a",Scale,"You are a 11 out of 10")
  print("Remeber you are amazing, go out and be a champ")
elif Think.lower()== "bad":
  print("Hello",name,"Imagine being you")
  print("Imagine wanting to Achieve",Achieve,)
  print("You are a",Scale,"out of 1000000000000000000000000000000000000000000000")
  print("You are failing everything,get a life")
  print("Whats the matter did i hurt your feelings womp womp")

else:
  print("Just type good or bad not that hard")