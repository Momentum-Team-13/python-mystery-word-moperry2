# from ast import Break
# from msilib.schema import File
import random

#Read text file and Select random word from generated list
def select_random_word(file):
    word_list = open(file, "r")
    random_word = random.choice(word_list.read().split())
    word_list.close()
    print(random_word)
    print('Can you guess a letter in the word??')
    print(len(random_word) * " _ ", end="")
    return random_word

secret_word = select_random_word("words.txt")
# print(secret_word)

# def play():
#     secret_word_length = len(secret_word) * '_ '
# # guessed = False
#     return secret_word_length
# for i in xrange(random.randrange(len(s))):
#     s = secret_word_length
#     return s
#show spaces for word being guessed

#get a guess
def guess_the_letter():
    user_guess = input(' Guess a letter: ')
    if user_guess.isalpha():
            #check if all the characters in the user's guess are alphabets
        # letter = user_guess
        return user_guess
        # if user_guess in guessed_letters:
        #     print("You already guess the letter", user_guess)
    else:
        print('That guess was not a letter')
    guess_the_letter()
#check guess
#if wrong increase count, loop until player has too many failed attempts
#print correct letters
#if correct break 
def play_game():
#loop thru 8 guesses
    letters_guessed = []
    failure_count = 8
    while failure_count > 0:

        guess = guess_the_letter()
        if guess not in {secret_word}:
            print(f"Correct!! There is one or more {guess}'s in the secrect word.")
        else: 
            failure_count -= 1
            print(f" Incorrect. There are no {guess}'s in the secret word. {failure_count} turn(s) left.")

    #maintain a list of all letters guessed
        letters_guessed = letters_guessed + guess.split()
        wrong_letter_count = 0
        for letter in secret_word:
            if letter in letters_guessed:
                print(letter, end="")
            else: 
                print(f" _ ", end="")
                wrong_letter_count =+ 1
        #if there were no wrong letters, the player wins
        if wrong_letter_count == 0:
            print(f" Congrats! The secret word was: {secret_word}. YOU WON!!")
            break
    else: 
        print("Sorry, you didn't win this time. Try again.")

if __name__ == "__main__":
    play_game()