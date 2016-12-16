import subprocess
import json
import random

# Parse a page using Scrapy
# https://docs.python.org/3/library/subprocess.html
def parse(scrapper_file, output_file):
    subprocess.run(["rm", "-rf", output_file])
    subprocess.run(["scrapy", "runspider", scrapper_file, "-o", output_file])

# Give a Json file and return a Dictionary
def open_json(file):
    with open(file) as f:
        data = json.load(f)
        return data

# Give a json and return a list
def store_in_list(json_input, list_output, key):
    # Store quotes on a list. Create an empty list and add each sentence one by one.
    for sentence in json_input:
        # Clean quotes from whitespace and so on
        s = sentence[key].strip()
        # don't use extend as it adds each letter one by one!
        list_output.append(s)

# Return a random item in a list
def random_item_in(list):
    rand_numb = random.randint(1, len(list))
    return list[rand_numb]  


#####################
###### QUOTES #######
#####################

def random_quote():
    json_quotes = open_json('s_a.json')
    quotes = []
    store_in_list(json_quotes, quotes, 'quote')
    return random_item_in(quotes) 

######################
#### CHARACTERS ######
######################

# Gather characters from Wikipedia

def random_character():
    json_characters = open_json('characters.json')
    characters = []
    store_in_list(json_characters, characters, 'character')
    return random_item_in(characters) 

######################
###### SENTENCE ######
######################

######################
#### INTERACTION ######
######################

# Print a random sentence.

def random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character, rand_quote))

def interaction():
    choice = input('Would you like another true quote? Type [enter] To exit, type [B]. To launch the scrapper again, type [C]').upper()
    if choice == 'B':
        quit()
    elif choice == 'C':
        parse('san_antonio_scrapper.py', 's_a.json')
        parse('characters_scrapper.py', 'characters.json')
    else:
        random_sentence()
        interaction()

if __name__ == '__main__':
    random_sentence()
    interaction()