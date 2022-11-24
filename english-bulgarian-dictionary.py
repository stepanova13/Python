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
    if word in dictionary:
        print(dictionary.get(word))
    # if word does not exist in the dictionary, print " 'word' not in my memory"
    else:                                
        print(f"{word_to_translate} is not in my memory")

# define a global vaeriable
word_to_translate = ''

while True:
    # ask user what word they want to translate and turn it lowercase
    word_to_translate = input("Type a word to translate: ").lower()
    # call the function to translate the word from the user input
    bulgarian(word_to_translate)
    # ask user if they want to translate another word
    another = input("Another? / NO-type 'n', YES - press enter\n").lower()
    if another == 'n':
        break



