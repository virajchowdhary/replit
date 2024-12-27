import os,time
print("To Do List Manager")
List = []
def PrettyPrint():
  os.system("clear")
  print("List:")
  print()
  for index in range(len(List)):
    print(f"{index+1}: {List[index]}")
def Look():
  print("To Do List")
  print()
  for item in List:
   print(item)
while True:
  menu = input("Do you want to view, add,remove or edit your to do list?: ")
  if menu.lower() == "view":
    print()
    PrettyPrint()
    time.sleep(10)
    os.system("clear")
  elif menu.lower() == "add":
    print()
    item = input("What do you want to add?: ")
    if item in List:
      print("This item is already in the list")
      time.sleep(2)
      os.system("clear")
    elif item not in List:
      List.append(item)
    time.sleep(1)
    os.system("clear")
  elif menu.lower() == "remove":
    print()
    item=input("What Item Do you Want to Remove?: ")
    if item not in List:
      print(f"{item} was not in the list")
      time.sleep(2)
      os.system("clear")
      continue
    Do = input("Are you sure you want to remove this item?: ")
    if Do.lower() == "yes":
      List.remove(item)
      if item in List:
        List.remove(item) 
        time.sleep(1)
        os.system("clear")
    elif Do.lower()=="No":
      print("bringing you back to the menu")
      time.sleep(2)
      os.system("clear")
    elif item not in List:
      print(f"{item} was not in the list")
  elif menu.lower() == "edit":
    PrettyPrint()
    print()
    item = input("What do you want to edit?: ")
    if item in List:
      List.remove(item)
      item = input("What do you want to change it to?: ")
      List.append(item)
      time.sleep(1)
      os.system("clear")
    elif item not in List:
      print(f"{item} was not in the list")
      time.sleep(2)
      os.system("clear")
    
  else:
    os.system("clear")