print("Math facts game")
number=int(input("Enter a number: "))
counter=0
for i in range(1,11):
  print(number,"x",i ,"=") 
  answer=int(input(""))
  if answer==number*i:
    print("Correct")
    counter+=1
  elif answer!=number*i:
    print("Incorrect")
print("You got",counter,"out of 10")