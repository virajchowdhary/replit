counter = 1
print("Lyric guesser(Basic)")
while True:
  print("Fill in the blanks form songs")
  print("Midnights______my afternoons ")
  Answer = input("Answer: ")
  if Answer.lower() == "become":
    print("Correct")
    print("it took",counter,"attempt(s)")
    break
  counter += 1