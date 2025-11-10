import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy',
               'white', 'proud', 'brave', 'black', 'dirty']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'horse', 'telephone', 'banana', 'teacher'
         'carrot', 'coconut']

print("--- Welcome to password generator! ---")

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 1000)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print(f"Your new password is: {password}")

    choice = input("Generate new password? (y/n): ")
    if choice == "n":
        break
