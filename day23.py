print("Login System")
def Loginsystem():
  while True:
    password=input("What is your password?")
    username=input("What is your username?")
    if username=="Viraj" and password=="BooksCool24":
      print("Welcome Viraj!")
      break
    else:
      print("Wrong try again")
      continue

Loginsystem()