import random
#Make list of words

#player picks one randomly from the list

#based on the length of the word, make dashes

#player2 gueses one letter from the word,
# if the letter is in the word,

# 1 . insert the letter in its place in the word
#if the letter is not in the word, add an ascia to the hang robe

#enclose in a while loop so :
#1. hangs and ends if the handman is fully drawn
#2. end and player 2 wins if the word completes

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.