print("Second in leap asnd not leap year calculator")
Year=input("Is it a leap year:")
minute=60*1
hour=60*minute
day=24*hour
month=(365/12)*day
year=month*12
answer=year+day
Answer=year
if Year.lower() =="yes":
  print("Number of seconds in a leap year are",answer,)
elif Year.lower()=="no":
  print("The number of seconds in a year are",Answer,)
else:
  print("Type yes or no it can even be Uppercase")
print("")
print("Leap year calculator")
year = int(input("Enter the year: "))
if year % 4 == 0 and year % 400 == 0:
  print("Leap year")
else:
  print("Not a leap year")