# -*- coding: latin-1 -*-

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]

def show_random_quote():
    # get a random number
    # get a quote from an array
    # show the quote in the interpreter
    pass

def show_random_item_in(my_list):
    # TODO: get a random number
    item = my_list[0] # get a quote from a list
    print(item) # show the quote in the interpreter
    return "program is over" # returned value

show_random_quote()
print(show_random_item_in(quotes))

user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')
# if user_answer == "B":
#     pass
# elif user_answer == "C":
#     print("C pas la bonne réponse ! Et G pas d’humour, je C...")
# else:
#     # show another quote
#     pass
