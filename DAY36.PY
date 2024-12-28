Name=[]
def NameList():
  for name in Name:
    print(name)
    print()
while True:
  First = input("Enter your first name: ").strip().capitalize()
  Last = input("Enter your last name: ").strip().capitalize()
  name= f"{First} {Last}"
  if name not in Name:
    Name.append(name)
  else:
    print("ERROR: Duplicate name")
    print()
  NameList()