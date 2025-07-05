# Problem A

def rps_winner(player, comp):
    '''
    Purpose:
        To determine number of points player receives in this round
    Parameter(s):
        player: (str) single-letter character that represents player's input, and it
        can be R, P, or S, representing rock, paper, or scissors respectively
        comp: (str) single-letter character that represents computer's input, and it
        can be R, P, or S, representing rock, paper, or scissors respectively
    Return Value:
        (int) value that represents number of points player receives, returns
        1, -1, or 0
    '''

    if player == 'R' and comp == 'P':
        return -1
    elif player == 'R' and comp == 'S':
        return 1
    elif player == 'P' and comp == 'R':
        return 1
    elif player == 'P' and comp == 'S':
        return -1
    elif player == 'S' and comp == 'P':
        return 1
    elif player == 'S' and comp == 'R':
        return -1
    else:
        return 0


if __name__ == '__main__':
    print(rps_winner('R', 'R'))  #Should output 0
    print(rps_winner('S', 'P'))  #Should output 1
    print(rps_winner('R', 'P'))  # Should output -1
    print(rps_winner('R', 'S'))  # Should output 1
    print(rps_winner('P', 'R'))  # Should output 1
    print(rps_winner('P', 'S'))  # Should output -1
    print(rps_winner('S', 'R'))  # Should output -1

#Problem B

def player_move():
    '''
    Purpose:
        To check whether user input is valid
    Parameter(s):
        None
    Return Value:
        (str) valid single-letter character that represents player's choice
    '''

    player_choice = input('Please enter your choice for the game(R, P, or S) = ')
    while not (player_choice == 'R' or player_choice == 'P' or player_choice == 'S'):
        print('Invalid Move')
        player_choice = input('Please enter your choice for the game again(R, P, or S) = ')
    return player_choice



# Problem C

def rps_game(num_rounds):
    '''

    Purpose:
        To conduct certain number of rounds of game, identify who wins in each round,
        and find the total score of the player, computer input is always the same
    Parameter(s):
        num_rounds: (int) number of rounds the game should be played
    Return Value:
        (int) value that represents total score of the player

    '''

    total_score = 0

    for round in range(1, num_rounds + 1):
        print(f'Round: {round}, Score: {total_score}' )
        player_input = player_move()
        print('Computer selects R')
        round_result = rps_winner(player_input, 'R')
        total_score += round_result
        if round_result == 1:
            print('Player Wins!')
        elif round_result == -1:
            print('Computer Wins!')
        else:
            print("Tie!")
    return total_score


# Problem D

def rps_game2(num_rounds):
    '''

    Purpose:
        To conduct certain number of rounds of game, identify who wins in each round,
        and find the total score of the player, employing better strategy to assign
        computer_input by picking whatever the player chose last time(R as default value)
    Parameter(s):
        num_rounds: (int) number of rounds the game should be played
    Return Value:
        (int) value that represents total score of the player

    '''
    total_score = 0
    computer_input = 'R'
    for round in range(1, num_rounds + 1):
        print(f'Round: {round}, Score: {total_score}')
        player_input = player_move()
        print(f'Computer selects {computer_input}')
        round_result = rps_winner(player_input, computer_input)
        total_score += round_result
        if round_result == 1:
            print('Player Wins!')
        elif round_result == -1:
            print('Computer Wins!')
        else:
            print("Tie!")
        computer_input = player_input
    return total_score









