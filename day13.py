print("Grade Calculator")
ScoreMax=int(input("What is the maximum score you could receive?"))
Score= int(input("What score did you get"))
Answer= (Score/ScoreMax)*100
Answer= round(Answer,2)
print("You got", Answer)
if Answer>=90 and Answer<=100:
  print("You got an A")
elif Answer<=89.99 and Answer>=86.99:
  print("You got a B+")
elif Answer<=86.98 and Answer>=82.99:
  print("You got a B")
elif Answer>=79.99 and Answer<=82.98:
  print("You got a B-")
elif Answer>=76.99 and Answer<=79.98:
  print("You got a C+")
elif Answer>=72.99 and Answer<=76.98:
  print("You got a C")
elif Answer>=69.99 and Answer<=72.98:
  print("You got a C-")
elif Answer>=66.99 and Answer<=69.98:
  print("You got a D+")
elif Answer>=59.99 and Answer<=66.98:
  print("You got a D")
elif Answer<=59.98:
  print("You got an N")
else:
  print("I dont count bonus questions if you did a bonus question good for you")