print("STAR WARS NAME GENERATOR")
Stuff=input("Enter your first name, last name, Mum's maiden name and the city you were born in with spaces:")
Stuff=Stuff.split()
print()
print(f"Your Star Wars name is {Stuff[0][0:3].title()}{Stuff[1][0:2].lower()} {Stuff[2][0:2].title()}{Stuff[3][-3:].lower()}")