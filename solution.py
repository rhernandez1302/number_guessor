import random
art =   """ _   __                __                 ______                              
   / | / /_  ______ ___  / /_  ___  _____   / ____/_  _____  _____________  _____
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / / __/ / / / _ \/ ___/ ___/ _ \/ ___/
 / /|  / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __(__  |__  )  __/ /    
/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      \____/\__,_/\___/____/____/\___/_/     
                                                                              """ 
def decrease_lives():
  return lives - 1

print(art)  
print("Welcome to guessing game")
random_num = random.randint(1,100)
choice = input("What difficulty would you like: easy or hard? ")
if choice == 'easy':
  lives = 10
  win = False
  while lives != 0:
    print(f"You have {lives} trys")
    guess = int(input("What number would you like to guess? "))
    if guess < random_num:
      print("Guess is too low")
      lives = decrease_lives()
    elif guess > random_num:
      print("Guess is too high")
      lives = decrease_lives()
    elif guess == random_num:
      print(f"Correct, the right number was {random_num}")
      lives = 0
      win = True
  if win == True:
    print("You win")
  else:
    print(f"You lose, the correct answer was {random_num}")
  
elif choice == 'hard':
  lives = 5
  win = False
  while lives != 0:
    print(f"You have {lives} trys")
    guess = int(input("What number would you like to guess? "))
    if guess < random_num:
      print("Guess is too low")
      lives = decrease_lives()
    elif guess > random_num:
      print("Guess is too high")
      lives = decrease_lives()
    elif guess == random_num:
      print(f"Correct, the right number was {random_num}")
      lives = 0
      win = True
  if win == True:
    print("You win")
  else:
    print(f"You lose, the correct answer was {random_num}")
