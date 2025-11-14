from nltk.corpus import wordnet as wn
import random

# Get all nouns
nouns = set()
for synset in wn.all_synsets('n'):
    for lemma in synset.lemmas():
        nouns.add(lemma.name())
# Get all adjectives
adjectives = set()
for synset in wn.all_synsets('a'):
    for lemma in synset.lemmas():
        adjectives.add(lemma.name())
# Special chars
chars = ["@", "-", "_", "!", "$", "&", "#", "%", "*"]

def random_case(word: str, flip_prob: float = 0.6) -> str:
    result = ""
    for ch in word:
        if ch.isalpha() and random.random() < flip_prob:
            ch = ch.upper() if ch.islower() else ch.lower()
        result += ch
    return result

def make_password(complexity: int):
    adjective = random.choice(list(adjectives))
    noun = random.choice(list(nouns))
    number = random.randrange(0, 1000)
    special_char = random.choice(chars)

    match complexity:
        case 1:
            password = str(adjective + noun).lower()
            password = password.replace('"', '').replace("'", "")
            result = ''.join(ch for ch in password if ch not in chars)
            return result
        case 2:
            password = adjective + noun + str(number)
            result = ''.join(ch for ch in password if ch not in chars)
            return result
        case 3:
            password = adjective + noun + special_char+ str(number)
            return password
        case 4:
            password = adjective + noun + special_char + str(number)
            return password.upper()
        case 5:
            password = adjective + noun + special_char + str(number)
            password = random_case(password)
            return password
        case _:
            print("Invalid Choice. Exiting.")

print("--- Welcome to password generator! ---")
while True:
    adjective = random.choice(list(adjectives))
    noun = random.choice(list(nouns))
    number = random.randrange(0, 1000)
    special_char = random.choice(chars)

    complexity = int(input("Choose a complexity level: \n1. You want to be hacked \n2. Maybe not \n3. This seems good \n4. Yeah, this ones secure \n5. You wanna be a hacker \nEnter your choice: "))
    password = make_password(complexity)
    print(f"Your new password is: {password}")

    choice = input("Generate new password? (y/n): ")
    if choice == "n":
        break
