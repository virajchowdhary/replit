counter = 0
while counter < 10:
  print(counter)
  counter +=1
exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")

Animals=""
while Animals.lower() != "dog" and Animals.lower() != "cat" and Animals != "horse":
  Animals = input("What animal do you want?: ")
  if Animals.lower() == "dog":
    print("Dog goes Woof")
  elif Animals.lower() == "cat":
    print("Cat goes Meow")
  elif Animals.lower() == "horse":
    print("Horse goes Neigh")
#correct code
#exit = "no"
#while exit == "no":
  #animal_sound = input("What animal sound do you want to hear?")

  #if animal_sound == "cow" or animal_sound == "Cow":
    #print("🐮 Moo")
  #elif animal_sound == "pig" or animal_sound == "Pig":
    #print ("🐷 Oink")
  #elif animal_sound == "sheep" or animal_sound == "Sheep":
    #print ("🐑 Baaa")
 # elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  #elif animal_sound == "dog" or animal_sound == "Dog":
    #print("🐶 Woof")
  #elif animal_sound == "cat" or animal_sound == "Cat":
    #print("🐱 Meow")
  #else: 
   #print("I don't know that animal sound. Try again.")
  #exit = input("Do you want to exit?: ")