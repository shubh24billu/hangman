import random
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
word_list = ["aardvark", "baboon", "camel", "megahertz", "haphazard", "pneumonia", "fluffiness", "jukebox", "curacao",
             "azure", "grogginess", "whiskey", "squawk"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

chosen_word_format = []
for _ in range(word_length):
    chosen_word_format += "_"
life = 6
end_game = False
while not end_game:
    guess = input("enter a letter you want to choose: ").lower()
    if guess in chosen_word_format:
        print("you have already chosen this letter")
    for i in range(word_length):
        if guess == chosen_word[i]:
            chosen_word_format[i] = guess
            life = life

    if guess not in chosen_word:
        life -= 1
        if life == 0:
            end_game = True
            print("you lose")
    print(chosen_word_format)
    print(life)
    print(stages[life])
    if "_" not in chosen_word_format:
        print("you have won the game")
        end_game = True



