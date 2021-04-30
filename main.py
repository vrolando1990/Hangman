import hangman_art
import random
import hangman_words

# Intro

print(hangman_art.logo)
print("Lets play some hangman!\nA word has been chosen, so lets go!")
print(hangman_art.stages[6])
print()

# Choose random word
word_letters = []
privious_picks = []
word = random.choice(hangman_words.word_list)

# Create blanked word spaces
for _ in word:
  word_letters.append("_")

# Request for a letter
print(word)
print(word_letters)
lives = 5

while "_" in word_letters and lives > -1:

  letter = input("Guess a letter: ").lower()

  if letter not in privious_picks:
    privious_picks.append(letter)

    if letter in word:
      print(f"\nGood job! The word does contain the letter \"{letter}\"")
      for position in range(len(word)):
        if word[position] == letter:
          word_letters[position] = letter
    else:
      print(f"\nSorry the word does not contain the letter \"{letter}\". You have lost a life.")
      print(hangman_art.stages[lives])
      lives -= 1
  else:
    print(f"\nYou have picked the letter \"{letter}\" already! Try again!")

  print(word_letters)

if "_" in word_letters:
  print(f"\nYou lose! The word was {word} ")
else:
  print(f"\nYou won! The word was {word}")
