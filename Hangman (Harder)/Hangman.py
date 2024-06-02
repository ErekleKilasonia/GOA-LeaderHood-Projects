import random
from Words import listn
import string

def valid_word():
    x = random.choice(listn)
    while " " in x or "-" in x:
        x = random.choice(listn)
    return x.upper()
    
def hangman():
    x = valid_word()
    word_letters = set(x)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 or lives != 0:
        if lives == 1:
            print(f"You have {lives} live left and used these letters: " + " ".join(used_letters))
        else:
            print(f"You have {lives} lives left and used these letters: " + " ".join(used_letters))
        listn = []
        for letter in x:
            if letter in used_letters:
                listn.append(letter)
            else:
                listn.append("-")
        print("Current word: " + " ".join(listn))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You have arleady used that letter.Please Try again another letter:")
        else:
            print("Invalid character.Please try again:")
    if lives == 0:
        print(f"You lost😢.Word was {x.capitalize()}.")
    else:
        print(f"You guessed the word!🎆😄 and this word was {x.capitalize()}.")

hangman()