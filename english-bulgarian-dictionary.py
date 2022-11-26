''' Writing a program that translates words from English to Bulgarian.
    Using function for translation. '''

# create the dictionary database
dictionary = {
            "hi" : "здравей",
            "bye" : "Чао",
            "goodbye" : "Довиждане",
            "yes" : "Да",
            "no" : "не",
            "day" : "ден",
            "green" : "зелено",
            "apple" : "ябълка",
            "potato" : "картоф",
            "prune" : "слива"
        }

# define finction to translate a word
def bulgarian(word):
    # if the word is in the dictionary
    if word in dictionary:
        # translate the word and display it on the screen
        print(dictionary.get(word))
    # if word does not exist in the dictionary, print " 'word' not in my memory"
    else:                                
        print(f"{word_to_translate} is not in my memory")

# create a while loop
while True:
    # ask user what word they want to translate and turn it lowercase
    word_to_translate = input("Type a word to translate: ").lower()
    # call the function to translate the word from the user input
    bulgarian(word_to_translate)
    # ask user if they want to translate another word and turn it lowercase
    another = input("Another? / NO-type 'n', YES - press enter\n").lower()
    # if answer is no, break out of the whole loop
    if another == 'n':
        break



