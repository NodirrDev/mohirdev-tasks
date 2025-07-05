# Problem A

def closest_price(guesses, true_cost):
    '''
    Purpose:
    To find out the winner who gets as close as possible to the answer
    but does not go over.
    Parameter(s):
    guesses - non-empty list of positive integers, stores guesses of contestants
    true_cost - integer, value that represents actual cost of an item
    Return Value:
    integer, value that represents prediction that is the closest to the actual price,
    and returns 0 if all guesses are over true_cost
    '''

    greater_arr = []
    for guess in guesses:
        if guess <= true_cost:
            greater_arr.append(guess)
    if len(greater_arr) == 0:
        return 0
    difference = true_cost - greater_arr[0]
    lowest = greater_arr[0]
    for x in greater_arr:
        if true_cost - x < difference:
            difference = true_cost - x
            lowest = x
    return lowest



# Problem B

def balance_name(first_names, last_names):
    '''
    Purpose:
    To determine every possible pair of first and last names with same number of characters
    from two lists
    Parameter(s):
    first_name - list of strings, list that stores first names
    last_name - list of strings, list that stores last names
    Return Value:
    list of strings that represents matching pairs of first and last names
    '''

    matching_names = []
    for first_name in first_names:
        for last_name in last_names:
            if len(first_name) == len(last_name):
                matching_names.append(f'{first_name} {last_name}')
    return matching_names



# Problem C

def score(word):
    '''
    Purpose:
    To determine total score based on how many consecutive letters word contains
    times length of the word
    Parameter(s):
    word - string, value that only contains uppercase letters
    Return Value:
    integer, value that represents total score
    '''

    doubles = 0
    for index in range(len(word) - 1):
        if word[index] == word[index + 1]:
            doubles += 1
    total_points = doubles * len(word)
    return total_points

# Problem D

def sort_double(wordlist):
    '''
    Purpose:
    To sort list based on how many scores each word in the list got, from highest to
    the lowest, using bubble sort
    Parameter(s):
    wordlist:
    list of string with uppercase words
    Return Value:
    list of the same words, ordered from the highest to the lowest
    '''

    for x in range(len(wordlist) - 1):
        for i in range(len(wordlist) - 1):
            if score(wordlist[i]) < score(wordlist[i + 1]):
                temp = wordlist[i]
                wordlist[i] = wordlist[i + 1]
                wordlist[i + 1] = temp

    return wordlist






































