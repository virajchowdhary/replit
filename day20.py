print("List Generator")
print("If go negativ use -")
i=int(input("What number to start at?"))
q=int(input("What number to end before?"))
a=int(input("Increment between values"))
for v in range(i,q,a):
  print(v)