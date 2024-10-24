#Final 
import os
import random

import day_7_word_list 
chosen_word = random.choice(day_7_word_list.word_list)
#or
#from day_7_word_list import word_list
#chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from day_7_art import logo
print (logo)

#Uncomment for Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    os.system('cls' if os.name == 'nt' else 'clear')

    
    if guess in display:
        print(f"You've already guessed {guess}.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the word.You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    import day_7_art
    print(day_7_art.stages[lives])