# from ast import Break
# from msilib.schema import File
import random
#Read text file and Select random word from generated list
def select_random_word(file):
    word_list = open(file, "r")
    random_word = random.choice(word_list.read().split())
    word_list.close()
    print(random_word)
    return random_word

secret_word = select_random_word("words.txt")
print(secret_word)

secret_word_length = len(secret_word)
for i in xrange(random.randrange(len(s))):
    s = secret_word_length
    return s
    # print(secret_word_length)
#show spaces for word being guessed

# letters_guessed = ""
# #loop thru 8 guesses
# failure_count = 8
# #get a guess
# #check guess
# #if wrong increase count, loop until player has too many failed attempts
# #print correct letters
# #if correct break 
# while failure_count > 0:

#     def play_game():
#         user_guess = input('Guess a letter: ')
#         if user_guess.isalpha():
#             letter = user_guess
#             return letter
#         else
#             print('That guess was not a letter')
#             #check if all the characters in the user's guess are alphabets
#         if user_guess in {File}:
#             print(f'Correct!! There is one or mpre {user_guess} in the secrect word.')
#         else: 
#             failure_count -= 1
#             print(f'Incorrect. There are no {user_guess} in the secret word. {failure_count} turn(s) left.')

# #maintain a list of all letters guessed
# letters_guessed = letters_guessed + user_guess
# wrong_letter_count = 0
# for letter in {File}:
#     if letter in letters_guessed:
#         print(f"(letter), end.")
#     else: 
#         print(f"'_', end.")
#         wrong_letter_count =+ 1

# #if there were no wrong letters, the player wins
# if wrong_letter_count == 0:
#     print(f"Congrats! The secreat word was: {File}. YOU WON!!")
#     break

if __name__ == "__main__":
    play_game()