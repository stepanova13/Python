
''' Writing a program that translates words from English to French or from English to Bulgarian '''

# create dictionary
dictionary = {
        "english to french" :

        {"green" : "verte",
        "worm" : "ver",
        "glass" : "verre",
        "unripe" : "vert",
        "prune" : "prune"},

        "english to bulgarian" :

        {"hi" : "здравей",
        "car" : "кола",
        "house" : "къща",
        "prune" : "слива"}
    }

# assign variables
# ask user which language they want
language = input("French or Bulgarian? ").lower()
# ask user what word they want to translate
word = input("word: ").lower()

if language != "french" and language != "bulgarian":
    print("Invalid input")
elif language == "french" and word in dictionary["english to french"]:
    print(dictionary["english to french"].get(word))

elif language == "bulgarian" and word in dictionary["english to bulgarian"]:
    print(dictionary["english to bulgarian"].get(word))
else:
    print(f"{word} is not in my memory")
