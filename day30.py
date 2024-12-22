print("30 Days Down What Do You Think")

for i in range(1,31):
  thought = input(f"Day {i}:\n")
  print()
  myText=f"You thought Day {i} was"
  Line2=f"{thought}"
  print(f"{myText:^35}")
  print(f"{Line2:^35}")
  print()