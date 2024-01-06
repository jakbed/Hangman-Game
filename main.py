import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
print("")
word = random.choice(word_list)
chosen_word = list(word)
lives = 6
display = ["_" for _ in chosen_word]

while "_" in display and lives > 0:
    guess = input("Give me a letter: ").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(stages[lives])
    print("")
    print(display)

if not "_" in display:
    print("Congratulations! You win!\n")
else:
    print(stages[0])
    print("Your word was: " + word + "\n")
    print("You lose, try again. \n")