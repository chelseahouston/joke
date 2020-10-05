def joker():
  number = input("Enter a number between 1-10 to get a Joke: ")
  try:
    number = int(number)
  except ValueError:
    print("Incorrect value. Please enter a Number.")
  if number == 1:
    print("I told my wife she was drawing her eyebrows too high.")
    print("She looked surprised.")
    print("----------")
  elif number == 2:
    print("What's the best thing about Switzerland?")
    print("I don't know but the flag is a big plus.")
    print("----------")
  elif number == 3:
    print("Why do we tell actors to 'break a leg'?")
    print("Because every play has a cast.")
    print("----------")
  elif number == 4:
    print("A man walks into a Zoo. The only animal is a dog.")
    print("It's a Shitzu.")
    print("----------")
  elif number == 5:
    print("What did the Pirate say when he turned 80?")
    print("Aye matey.")
    print("----------")
  elif number == 6:
    print("Did you guys hear the the joke about the high wall?")
    print("I'm still trying to get over it!")
    print("----------")
  elif number == 7:
    print("Why is Peter Pan always flying?")
    print("He neverlands.")
    print("----------")
  elif number == 8:
    print("What's the difference between England and a tea bag?")
    print("A tea bag stays in the cup longer.")
    print("----------")
  elif number == 9:
    print("What did one plate say to the other plate?")
    print("Dinner is on me!")
    print("----------")
  elif number == 10:
    print("Why was 6 afraid of 7?")
    print("because 7, 8, 9.")
    print("----------")
  elif number < 1:
    print("Please enter a number between 1-10")
    joker()
  elif number > 10:
    print("We don't have that many jokes yet! Please enter a number between 1-10")
    joker()
  else:
    print("Incorrect Value. Please enter a number between 1-10")
    joker()
# RUN AGAIN? ---
def run():
  while True:
    runagain = input("Run again? (Y/N): ").upper()
    if runagain not in ('Y', 'N'):
      print("Invalid Input.")
      run()
      break
    if runagain == 'Y':
      joker()
      run()
      break
    else:
      print("Thank you for playing Have a good day.")
      break

joker()
run()
