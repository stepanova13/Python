
''' Writing a program that translates words from English to French or from English to Bulgarian '''

# create dictionary
dictionary = {
        "english to french" :
        {
            "green" : "verte",
            "worm" : "ver",
            "glass" : "verre",
            "unripe" : "vert",
            "prune" : "prune"
        },
        "english to bulgarian" :
        {
            "hi" : "здравей",
            "car" : "кола",
            "house" : "къща",
            "prune" : "слива"
        }
    }

# assign variables
language = input("French or Bulgarian? ").lower()     # ask user which language they want and turn it lowercase
word = input("word: ").lower()                        # ask user what word they want to translate and turn it lowercase
french = dictionary["english to french"]              # simplify dictionary search
bulgarian = dictionary["english to bulgarian"]

# If the language is not French or Bulgarian, print "Invalid input"
if language != "french" and language != "bulgarian":  
    print("Invalid input")
# if language is French or Bulgarian, fetch the translated word from the dictionary
elif language == "french" and word in french: 
    print(french.get(word))
elif language == "bulgarian" and word in bulgarian:
    print(bulgarian.get(word))
# if word does not exist in the dictionary, print "word not in my memory"
else:                           
    print(f"{word} is not in my memory")
