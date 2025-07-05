#Problem A

def complement(dna_strand):
    '''
    Purpose: to form complement of dna strand,
    C and G are complements, as are A and T.
    Parameter(s):
        dna_strand: (str) value containing A, T, C, G characters
        representing dna strand
    Return Value: (str) value that represents complement
    of the given dna_strand
    '''

    new_string_complement = ''
    for base in dna_strand:
        if base == 'A':
            new_string_complement += 'T'
        elif base == 'T':
            new_string_complement += 'A'
        elif base == 'C':
            new_string_complement += 'G'
        elif base == 'G':
            new_string_complement += 'C'
    return new_string_complement





# Problem B

def correct_word(text):
    '''
    Purpose: Corrects a single incorrect letter in a given word
    Parameter(s):
        text: (str) A string of lowercase letters representing the
        English word we want to correct.
    Return Value:
        (str) A word that’s at most one letter away from the given
        text, if one can be found in words.txt.  Or '???' if not.
    '''
    fp = open('words.txt')
    common_words = fp.read().split()
    fp.close()

    if text in common_words:
        return text

    same_length = []
    length_text = len(text)
    for word in common_words:
        if len(word) == length_text:
            same_length.append(word)

    for word in same_length:
        counter = 0
        for x in range(length_text):
            if text[x] != word[x]:
                counter += 1
        if counter == 1:
            return word

    return '???'


# Problem C

def correct_all(sentence):
    '''
    Purpose: To correct the words in sentence using correct_word function,
             first word should be capitalized and there should be period
             at the end
    Parameter(s):
        sentence: (str) value representing full sentence, first letter
        is capitalize and period at the end
    Return Value:
        (str) value with the changes described in purpose

    '''
    words = sentence.split()
    words[0] = words[0].lower()
    words[-1] = words[-1][:len(words[-1]) - 1]

    for x in range(len(words)):
        words[x] = correct_word(words[x])

    words[0] = words[0].capitalize()
    words[-1] += '.'

    full_sentence = ' '.join(words)

    return full_sentence

# Problem D

def correct_word2(text):
    '''
    It is the same as correct_word, correct_all2 is different
    from correct_all.
    '''
    fp = open('words.txt')
    common_words = fp.read().split()
    fp.close()

    if text in common_words:
        return text

    same_length = []
    length_text = len(text)
    for word in common_words:
        if len(word) == length_text:
            same_length.append(word)

    for word in same_length:
        counter = 0
        for x in range(length_text):
            if text[x] != word[x]:
                counter += 1
        if counter == 1:
            return word

    return '???'

def correct_all2(sentence):
    '''
    correct_all is changed so that function is able to handle
    capitalization in places other than the beginning of the text.
    '''
    words = sentence.split()
    words[-1] = words[-1][:len(words[-1]) - 1]
    indexes_of_capitalized_words = []

    for x in range(len(words)):
        if words[x][0].isupper():
            words[x] = words[x].lower()
            indexes_of_capitalized_words.append(x)


    for x in range(len(words)):
        words[x] = correct_word2(words[x])

    for x in indexes_of_capitalized_words:
        words[x] = words[x].capitalize()
    words[-1] += '.'

    full_sentence = ' '.join(words)

    return full_sentence


if __name__ == '__main__':
    # What Is the ???.
    print(correct_all2('What Is the Differynce.'))

    # There Are Many ???.
    print(correct_all2('Thede Are Many error.'))


















