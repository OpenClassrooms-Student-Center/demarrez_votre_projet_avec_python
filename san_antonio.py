import subprocess
import json
import random

#####################
###### QUOTES #######
#####################

# Gather quotes and put them into quotes.json
# https://docs.python.org/3/library/subprocess.html
def get_quotes():
    subprocess.run(["rm", "-rf", "quotes.json"])
    subprocess.run(["scrapy", "runspider", "san_antonio_scrapper.py", "-o", "s_a.json"])

# Load quotes from a CSV file
with open('s_a.json') as f:
    data = json.load(f)

# Store quotes on a list. Create an empty list and add each sentence one by one.
quotes = []

for sentence in data:
    # Clean quotes from whitespace and so on
    s = sentence['quote'].strip()
    # don't use extend as it adds each letter one by one!
    q = quotes.append(s)

# Get any random quote
rand_numb = random.randint(1, len(quotes))
random quote = quotes[]

######################
###### POLITICS ######
######################

# Gather politics

# Gather dates

# Harmonise politics names

# Create a dictionnary out of quotes and politics on this format: 
# quotes = {'thatcher': {'quotes': ['Quote 1', 'Quote 2', 'Quote 3'], 'name': 'Thatcher'}}
# quotes['thatcher']['quotes']

# String creation, like "Thatcher said, in 1300: Quote"

# Randomly show one when we launch the program.

# Propose to launch the program again to have another quote. 
# We should ask him to refresh quotes and politics names.