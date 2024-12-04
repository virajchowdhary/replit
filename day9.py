myScore =int (input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
  
myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
    print("Exactly!")
else:
    print("Try again 😭")
print("")
print("Generation Identefier(Made in 2024 May not be up to date))")
MyYear=int(input("Which year were you born in? "))
if MyYear>=1883 and MyYear<=1900:
  print("Lost Generation")
elif MyYear>=1901 and MyYear<=1927:
  print("Greatest Generation")
elif MyYear>=1928 and MyYear<=1945:
  print("Silent Generation")
elif MyYear>=1946 and MyYear<=1964:
  print("Baby Boomers")
elif MyYear>=1965 and MyYear<=1980:
  print("Generation X")
elif MyYear>=1981 and MyYear<=1996:
  print("Millenials")
elif MyYear>=1997 and MyYear<=2012:
  print("Generation Z")
elif MyYear>=2013 and MyYear<=2024:
  print("Generation Alpha")
else:
  print("Sorry could not find your generation")