import random

def get_number_to_guess():
  computer_number = random.randint(1, 100)
  # pick a number "randomly" for user to guess -> not random enough for cryptography
  return computer_number

def guess_the_number():
  user_guess = input('Guess a whole number: ')
  # get user's guess as a string
  if user_guess.isdigit():
    #check if all the characters in the user's guess are numbers
    number = int(user_guess)
    # print(f'The number is: {number}, of the type {type(number)}')
    return number
    # print shows values in the console for the developer  
  else:
    # if the guess isn't a number
    print("That guess wasn't a number.")
    guess_the_number()

def play_game():
  user_guess = guess_the_number()
  computer_number = get_number_to_guess()

  while user_guess != computer_number:
    if user_guess < computer_number:
      print('Nah, the number is higher, try again.')
      user_guess = guess_the_number()
    elif user_guess > computer_number:
      print('Nah, the number is lower, try again.')
      user_guess = guess_the_number()

  print('You got it right! GG!')

play_game()
