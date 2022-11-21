
''' Writing a program that translates words from English to French or from English to Bulgarian '''

# create dictionary
dictionary = {
        "english to french" :
        {
            "hi" : "salut",
            "hello" : "bonjour",
            "bye" : "au revoir",
            "day" : "journée",
            "green" : "verte",
            "apple" : "pomme",
            "potato" :"pomme de terre",
            "prune" : "prune",
        },
        "english to bulgarian" :
        {
            "hi" : "здравей",
            "bye" : "чао",
            "goodbye" : "Довиждане",
            "day" : "ден",
            "green" : "зелено",
            "apple" : "ябълка",
            "potato" : "картоф",
            "prune" : "слива"
        }
    }

# assign variables
language = input("French or Bulgarian? ").lower()     # ask user which language they want and turn it lowercase
word = input("word: ").lower()    # ask user what word they want to translate and turn it lowercase
                    
french = dictionary["english to french"].get(word)              # translate the word in the French dictionary
bulgarian = dictionary["english to bulgarian"].get(word)        # translate the word in the Bulgarian dictionary

# If the language is not French or Bulgarian, print "Invalid input"
if language != "french" and language != "bulgarian":  
    print("Invalid input")
elif language == "french":     # if language is French or Bulgarian and the word is in the dictionary, fetch the translated word from the dictionary
    print(french)
elif language == "bulgarian":
    print(bulgarian)
else:                                            # if word does not exist in the dictionary, print "word not in my memory"
    print(f"{word} is not in my memory")
