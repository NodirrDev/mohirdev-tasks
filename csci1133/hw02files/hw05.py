
# Problem A

def expo(base, power):
    '''
    Purpose: Computes an exponent using only repeated addition
    Parameters:
        base: The base of the exponent (int, must be positive)
        power: The power of the exponent (int, must be positive)
    Return Value:
        A value equivalent to base**power (int)
    '''
    product = 1
    i = 0
    while i < power:
        total = 0
        j = 0
        while j < base:
            total += product
            j += 1
        product = total
        i += 1
    return product

if __name__ == '__main__':
    print(expo(3, 4)) #should output 81


# Problem B

def population(small, mid, big):
    '''
    Purpose: Identifies the number of weeks for any of fish types to become less than 10
    Parameters:
        small: (int) value that represents number of smallfish in the lake during some week
        mid: (int) value that represents number of middlefish in the lake during some week
        big: (int) value that represents number of bigfish in the lake during some week
    Return Value:
        (int)A value that represents number of weeks for any of fish types to become less than 10
    '''
    count = 0


    while not(small < 10 or mid < 10 or big < 10 or count == 30):
        count += 1
        new_small = int(1.1 * small - 0.0002 * small * mid)
        new_mid = int(0.95 * mid + 0.0001 * small * mid - 0.00025 * mid * big)
        new_big = int(0.9 * big + 0.0002 * mid * big)
        small = new_small
        mid = new_mid
        big = new_big
        print(f'Week {count} - Small: {small} Middle: {mid} Big: {big}')

    return count



# Problem C

def  durdle_check(guess, target):
    '''
    Purpose: checks how close the use choice matches actual target
    Parameters:
        guess: (str) five-character string that represents user choice
        target: (str) five_character string that represents actual target to be found
    Return Value:
        five-character string that shows whether characters in guess are found in target, are in the same
        location or does not exist(str)
    '''
    result = ""
    index = 0
    for x in guess:
        if guess[index] == target[index]:
            result += "G"
        elif x in target:
            result += "Y"
        else:
            result += "B"
        index += 1
    return result


# Problem D

def durdle_game(target):
    '''
    Purpose: Prompting user to input guesses until they find the target
    Parameters:
        target: five-character string that needs to be found(str)
    Return Value:
        number of guesses that it takes for user to input actual target(int)
    '''
    print("Welcome to Durdle!")
    count = 0
    game_result = ""
    while not (game_result == "GGGGG"):
        user_choice = input("Enter a guess:")
        game_result = durdle_check(user_choice, target)
        count += 1
        print(game_result)

    print(f"Congratulations, you got it in {count} guesses!")
    return count
































