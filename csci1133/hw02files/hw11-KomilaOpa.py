
# Problem A

def merge(left, right):
    if left == '':
        return right
    elif right == '':
        return left
    elif left[0] <= right[0]:
        return left[0] + merge(left[1:], right)
    else:
        return right[0] + merge(left, right[1:])

def merge_sort(st):
    if len(st) <= 1:
        return st
    else:
        left = st[:len(st)//2]
        right = st[len(st)//2:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


'''
1. What are the base cases of the merge function?
Why is the return value for those cases correct?

if left == []:
        return right
    elif right == []:
        return left

The base cases of the merge function works when
left or right is empty. The return value is correct 
because if one list is empty, the other list is already 
sorted and can be returned. 

2. Describe what the recursive cases of merge are
doing to move towards the base case.

They compare the first elements of left 
and right, append the smaller one to the result. 
This process continues with the other elements of list. As length of
list reduces, it moves towards the base  case. 

3. What is the base case of the merge_sort function?
Why is the return value for that case correct?
if len(sequence) <= 1:
        return sequence
if length is less than or equal to one, it is already sorted, thus it can be 
returned. 

4. Describe what the recursive case of merge_sort 
does to move towards the base case.
It divides the list in half, then it sorts both
halves using recursion. Then merges sorted halves. As size of each recursive
problem reduces, it moves towards the base case. 

'''


#problem B


def collatz(n):
    '''
    Purpose:
    Identifies the Collatz sequence that starts from given n and ends at 1.
    If n is even, the next number is equal to n divided by 2. If n is odd, the next
    number is equal to 3 times n plus 1.
    This continues until the number becomes 1.

    Parameter:
    n (int): A positive integer that starts the sequence

    Returns:
    list: A list of numbers from n to 1 according to the Collatz rule
    '''
    if n == 1:
        return [1]
    else:
        if n % 2 == 0:
            next_n = n // 2
        else:
            next_n = 3 * n + 1
        return [n] + collatz(next_n)


# Problem C

def closest_price(guesses, true_cost):
    '''
    Purpose:
    Finds the guess that is closest to the true cost without going over.
    If all guesses are higher than true_cost, returns 0.

    Parameters:
    guesses (list): List of positive integers (guesses)
    true_cost (int): The actual price

    Returns:
    int: Best guess without going over, or 0 if there is none.
    '''
    if guesses == []:
        return 0
    else:
        best_rest_guess = closest_price(guesses[1:], true_cost)

        if guesses[0] > true_cost:
            return best_rest_guess
        else:
            if best_rest_guess > guesses[0]:
                return best_rest_guess
            else:
                return guesses[0]


# Problem D

import os
def get_files(path):
    '''
        Purpose:
        With help of recursion, all the text files in the given directory and
        its subdirectories are printed and counted
        Parameter(s):
        path: (str), folder path
        Return Value: int, total number of text files in the given folder
        '''
    count = 0
    for file in os.listdir(path):
        if os.path.isfile(path + '/' + file):
            if file.endswith('.txt'):
                print(path + '/' + file)
                count += 1
        else:
            sub_path = path + '/' + file
            count = count + get_files(sub_path)
    return count














































