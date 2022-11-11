
language = input("French or Bulgarian? ")
language = language.lower()

word = input("word: ")
word = word.lower()

english_to_french_dictionary = {
    "green" : "verte",
    "worm" : "ver",
    "glass" : "verre",
    "unripe" : "vert",
    "prune" : "prune"
    }

english_to_bulgarian_dictionary = {
    "hi" : "здравей",
    "car" : "кола",
    "house" : "къща",
    "prune" : "слива"
    }

if language == "french":
    if word in english_to_french_dictionary:
        print(english_to_french_dictionary.get(word))
    else:
        print(f"{word} is not in my memory")
elif language == "bulgarian":
    if word in english_to_bulgarian_dictionary:
        print(english_to_bulgarian_dictionary.get(word))
    else:
        print(f"{word} is not in my memory")
else:
    print("Invalid input")
