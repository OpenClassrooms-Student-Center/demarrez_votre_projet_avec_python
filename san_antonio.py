# -*- coding: utf8 -*-

quotes = [
    "ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "on doit pouvoir choisir entre s'écouter parler et se faire entendre."
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

def capitalize(quotes):
    # this function will not do anything for the moment.
    for quote in quotes:
        quote.capitalize()

def get_random_quote():
    # get a random number
    # get a quote from an array
    # show the quote in the interpreter
    pass

def get_random_item_in(my_list):
    # get a random number
    item = my_list[0] # get a quote from a list
    return item # return the item

user_answer = "A"

while user_answer != "B":
    print(get_random_item_in(quotes))

# if user_answer == "B":
#     pass
# elif user_answer == "C":
#     print("C pas la bonne réponse ! Et G pas d’humour, je C...")
# else:
#     # show another quote
#     pass
