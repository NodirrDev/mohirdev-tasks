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
1. Base case:
    if left == []:
        return right
    elif right == []:
        return left
These return the non-empty list when
the other is empty, which is correct because
an empty list merged with a sorted list is just the sorted list itself.
It does not have any effect.
2. They compare the first elements of left 
and right, append the smaller one to the result, 
and continue with the rest of that list. This reduces 
the size of one of the lists, moving toward the base case.
3. Base case:
    if len(sequence) <= 1:
        return sequence
A list of length 0 or 1 is already sorted, so it's correct to return it as-is.
4. It splits the list in half, recursively sorts both
halves, then merges the sorted halves. This reduces 
the size of each recursive problem, and moves it toward the base case.
'''

# Problem B

def collatz(n):
    '''
    Purpose:
    To create a list of integers that leads to 1 according to collatz theorem.
    n is the starting integer. If n is even, next integer is equal to n // 2,
    if n is odd next integer is equal to 3n + 1. We keep finding next integer
    and collect them in list until the value is 1.
    Parameter(s):
    n: (int) starting integer
    Return Value:
    list of integers. list with integers as described in purpose.
    '''

    if n == 1:
        return [1]
    else:
        if n % 2 == 0:
            return [n] + collatz(n//2)
        else:
            return [n] + collatz(3 * n + 1)

# Problem C

def closest_price(guesses, true_cost):
    '''
    Purpose:
    Checks list guesses recursively to find the guess that is closest to
    true_cost but not over it. Function returns 0 if all the guesses are more than
    true_cost.
    Parameter(s):
    guesses: non-empty list of positive integers, stores tha guesses of contestants
    true_cost: integer, actual price
    Return Value:
    integer, value that is closest to true cost but not over it. returns 0
    if all guesses are over true_cost.
    '''

    if guesses == []:
        return 0
    else:
        if guesses[0] <= true_cost:
            return max(guesses[0], closest_price(guesses[1:], true_cost))
        else:
            return closest_price(guesses[1:], true_cost)



# Problem D

import os
def get_files(path):
    '''
    Purpose:
    With recursion, counts and prints all the text files in the given directory and
    its subdirectories
    Parameter(s):
    path: string, directory path
    Return Value: int, total number of text files in the given directory
    '''

    count = 0
    for file in os.listdir(path):
        if os.path.isfile(path+'/'+file):
            if file.endswith('.txt'):
                print(path+'/'+file)
                count += 1
        else:
            sub_path = path+'/'+file
            count = count + get_files(sub_path)
    return count






















