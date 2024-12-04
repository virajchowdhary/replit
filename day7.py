print("Fake harry potter fan finder always type answers lowercase")
Harry = input(
    "Who is the main charecter in harry potter? and what is his full name:")
answer = False
print_exit_message = True

if Harry == "harry potter" or Harry == "harry james potter":
  print("correct but that was simple")
  answer = True

  Harry2 = input("what is harrys patronus?:")
  if Harry2 == "stag":
    print("So Anybody who read up to book 3 knows that")
  else:
    answer = False

  if answer is True:
    Harry3 = input("what is harry's mother's full name name?:")
    if Harry3 == "lily potter":
      print("A baby knows that")
    else:
      answer = False

  if answer is True:
    Harry4 = input("what is harry's father's full name name?:")
    if answer is True and Harry4 == "james potter":
      print("you know a bit")
    else:
      answer = False

  if answer is True:
    Harry5 = input("How many books are there:")
    if Harry5 == "7":
      print("Easily the simplest question")
      print_exit_message = False
    else:
      answer = False

  if answer is True:
    Harry6 = input(
        "What is the name of the creature guarding the Philosopher's Stone:")
    if Harry6 == "fluffy":
      print("you are a great fan")
    else:
      print("Dont feel bad you got the first 5")
      answer = False

  if answer is True:
    Harry7 = input("How many players are on a Quidditch team?:")
    if Harry7 == "7":
      print("you are a true fan")
    else:
      print("you are a great fan dont fell bad you got true 6 questions")
      answer = False

if print_exit_message is True:
  print("You are a fake fan. Leave!!!")
