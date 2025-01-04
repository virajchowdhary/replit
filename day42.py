print("Mokebeast")
Beast = {"Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}
for name, value in Beast.items():
  Beast[name] = input(f"{name}:\t").strip().title()
if Beast["Type"]=="Earth":
  print("\033[32m", end="")
elif Beast["Type"]=="Air":
  print("\033[37m", end="")
elif Beast["Type"]=="Fire":
  print("\033[31m", end="")
elif Beast["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")
for name, value in Beast.items():
  print(f"{name:<15}: {value}")