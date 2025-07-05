# Problem A
import random


def total_cost(order, prices):
    '''
    Purpose:
        To calculate the total cost of order
    Parameter(s):
        order: (dictionary) dictionary that contains food
        items (strings) as keys, and how many of each
        item a customer wants to buy (ints) as values
        prices: (dictionary) dictionary that contains
        various food items available at the store as
        keys, and their unit cost in dollars (floats)
        as the associated value
    Return Value:
        Cost of customer's order(float)
    '''

    total_cost = 0
    for item in order:
        total_cost += order[item] * prices[item]
    return total_cost


# Problem B

def follows(text):
    '''
    Purpose:
        To determine words that follow a particular word in the text,
        last word is not counted as there is no word following that
        word
    Parameter(s):
        text: (string) value representing some english text
    Return Value:
        (dictionary) each key in the output dictionary is a word
        from string text, and each value is a list of all of the
        words that directly follow that word
    '''

    out = {}
    words = text.split()
    for x in range(len(words) - 1):
        if words[x] in out:
            out[words[x]].append(words[x + 1])
        else:
            out[words[x]] = [words[x + 1]]
    return out

# Problem C

def suggest(current, follows_dict):
    '''
    Purpose:
        To determine what word would come after current word using
        dictionary follows_dict
    Parameter(s):
        current: (string) a single word
        follows_dict: (dictionary) dictionary where each key in is a word,
        and each value is a list of all of the
        words that directly follow that word
    Return Value:
        (list) suggested words to potentially follow current
        in a randomly generated sentence. If current word is not in
        follows_dict, returns a list of all keys
    '''

    all_keys = list(follows_dict.keys())
    if current in follows_dict:
        return follows_dict[current]
    else:
        return all_keys


# Problem D

def random_sent(filename, max_length):
    '''
    Purpose:
        To create a sentence of given length, starting word is chosen at random.
        next words is going to be determined with follows and suggest functions.
        Also sentence is completed when there is word ending with  a period,
        exclamation point, or question mark.
    Parameter(s):
        filename: (string) name of the file
        max_length: maximum length of the file
    Return Value:
        (string) sentence with characteristics described in purpose
    '''

    out_sentence = ''
    fp = open(filename)
    text = fp.read()
    follows_dict = follows(text)
    words = text.split()
    current_word = random.choice(words)
    counter = 0
    while counter < max_length:
        counter += 1
        out_sentence += current_word + ' '
        next_word = random.choice(suggest(current_word, follows_dict))
        if current_word[-1] == '!' or current_word[-1] == '?' or current_word[-1] == '.':
            counter = max_length
        current_word = next_word

    return out_sentence
























