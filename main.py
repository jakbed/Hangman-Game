import random

word_list = ["floord", "christmas", "icebraker"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = list(random.choice(word_list))
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
        print(stages[lives+1])
    
    print(display)

if not "_" in display:
    print("Congratulations! You win!\n")
else:
    print(stages[0])
    print("You lose, try again.")