#!/usr/bin/env python3
# A function that returns minimum value of an array of integers
# Approach 1 using built in functions

def ret_min(arr: list)-> int:
    '''
    Return a minimum value in an array of integers
    '''
    return min(arr)

#Driver code
if __name__ == '__main__':
    T = int(input()) # Number of test cases
    for idx in range(T):
        arr = list(map(int, input().split()))
        print(ret_min(arr))
