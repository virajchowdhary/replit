import os,time
print("To Do List Manager")
List = []
def Look():
  print("To Do List")
  print()
  for item in List:
   print(item)

while True:
  menu = input("Do you want to view, add, or edit your to do list?: ")
  if menu.lower() == "view":
    print()
    Look()
    time.sleep(10)
    os.system("clear")
  elif menu.lower() == "add":
    print()
    item = input("What do you want to add?: ")
    List.append(item)
    time.sleep(1)
    os.system("clear")
  elif menu.lower() == "edit":
    print()
    item=input("What Item Do you Want to Remove?: ")
    if item in List:
      List.remove(item) 
      time.sleep(1)
      os.system("clear")
    else:
      print(f"{item} was not in the list")
  else:
    os.system("clear")