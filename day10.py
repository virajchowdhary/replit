adding = 4 + 3
print(adding)
subtraction = 8 - 9
print(subtraction)
multiplication = 4 * 32
print(multiplication)
division = 50 / 5
print(division)
squared = 5**2
print(squared)
modulo = 15 % 4
print(modulo)
divisor = 15 // 2
print(divisor)
print("")
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer, "each")
print("")
print("Tip calculator")
Spend = float(input("How much did you spend?:"))
Percent = int(input("What percentage do you want to tip?:"))
People = int(input("How many people in your group?:"))
Tip = Spend / 100 * Percent
Answer = (Spend + Tip) / People
Answer = round(Answer, 2)
print("You each owe", Answer)
