import random
import os

def wordpicker(words):
    file = open(words + ".txt", "r")
    wordlist = []
    for line in file:
        line = line.strip("\n")
        wordlist.append(line)
    word_index = random.randrange(0,len(wordlist))
    chosen_word = wordlist[word_index]
    return chosen_word

def lettercheck(letter, wordlist):
  if letter in wordlist:
    return True
  else:
    return False

def letterchange(word_letters, guessed_letters, letter):
  for i in range(len(guessed_letters)):
    if word_letters[i] == letter:
      guessed_letters[i] = letter

def validator(letter):
  if letter.isalpha() == True and len(letter) == 1:
    return True
  else:
    return False

def wordvalidator(word):
  count = 0
  for letter in word:
    if letter.isalpha() == True:
      count += 1
  if count == len(word):
    return True
  else:
    return False

lives = 10
gamemodes = [1,2]
print("HANGMAN: GUESS THE WORD - 1 / CHOOSE THE WORD: 2\n")
gamemode = int(input("CHOOSE OPTION 1 OR OPTION 2: "))
while gamemode not in gamemodes:
  print("ENTER A VALID GAMEMODE CHOICE: ")
  gamemode = int(input("CHOOSE OPTION 1 OR OPTION 2: "))
if gamemode == 1: 
  word_letters = []
  guessed_letters = []
  wrong_letters = []
  word = wordpicker("/Users/ben/Code/Projects/Hangman/dictionary")
  for letter in word:
    guessed_letters.append("_")
    word_letters.append(letter)
  while word_letters != guessed_letters:
    os.system("clear")
    print("HANGMAN!\n")
    print("WORD LENGTH:", len(word), "\n")
    print("REMAINING LIVES: ", lives, "\n")
    print(" ".join(guessed_letters), "\n")
    if len(wrong_letters) > 0:
      print("WRONG LETTERS:", " ".join(wrong_letters), "\n")
    letter = input("ENTER A LETTER: ").upper()
    print("\n")
    valid = validator(letter)
    if valid == True:
      check = lettercheck(letter, word_letters)
      if check == True:
        letterchange(word_letters, guessed_letters, letter)
      else:
        if letter not in wrong_letters:
          wrong_letters.append(letter.upper())
          lives -= 1
    else:
        continue
    if lives == 0:
        print("YOU LOSE! YOUR WORD WAS: ", word)
        break
  if lives != 0:
    print("YOU WIN!\n" + word)

if gamemode == 2:
  chosen_letters = []
  cpu_guessed = []
  cpu_wrong = []
  chosen_word = input("CHOOSE A WORD FOR THE COMPUTER TO GUESS: ").upper()
  while wordvalidator(chosen_word) == False:
    print("INVALID WORD. TRY AGAIN\n")
    chosen_word = input("CHOOSE A WORD FOR THE COMPUTER TO GUESS: ").upper()
  alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  for letter in chosen_word:
    cpu_guessed.append("_")
    chosen_letters.append(letter)
  while cpu_guessed != chosen_letters:
    os.system("clear")
    print("CPU IS PLAYING...\n")
    print("YOUR WORD:", chosen_word, "\n")
    print(" ".join(cpu_guessed), "\n")
    if len(cpu_wrong) > 0:
      print("WRONG LETTERS:", " ".join(cpu_wrong), "\n")
    cpu_index = random.randrange(0, len(alphabet))
    alpha_index = alphabet[cpu_index]
    print("IS", alpha_index, "IN THE WORD?\n")
    alphabet.pop(cpu_index)
    yesno = int(input("YES? - 1 / NO? - 2: "))
    while yesno not in gamemodes:
      print("INVALID CHOICE. TRY AGAIN")
      yesno = int(input("YES? - 1 / NO? - 2: "))
    if yesno == 1:
      for i in range(len(chosen_letters)):
          if chosen_letters[i] == alpha_index:
                cpu_guessed[i] = alpha_index
    else:
      cpu_wrong.append(alpha_index)
      lives -= 1
      continue
    if lives == 0:
        print("YOU WIN! YOUR WORD WAS: ", chosen_word)
        break
  if lives != 0:
    print("COMPUTER WINS!\n" + chosen_word)