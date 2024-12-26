import os, time
listOfEmail = []
def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)):
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(10)
def spam():
  for i in range(0,10):
    print(f"email {listOfEmail[i+1]},")
    print(f"Dear {listOfEmail[i]}")
    print("It has come to our attention that you're missing out on")
    print("the amazing Replit 100 days of code. We insist you do it right away.") 
    print("If you don't we will pass on your email address to every spammer we've ever encountered and also") 
    print("sign you up to the My Little Pony newsletter, because")
    print ("that's neat. We might just do that anyway.")
    print()
    print("Love and hugs,")
    print("Ian Spammington III")
    time.sleep(10)
    os.system("clear")
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    os.system("clear")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    os.system("clear")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  elif menu == "4":
    spam()
  else:
    print("Invalid input pick 1, 2, 3, or 4")