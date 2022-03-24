#!/usr/bin/env python3
# A function that returns minimum value of an array of integers
# Approach 2

def ret_min(arr: list)-> int:
    '''
    Return a minimum value in an array of integers
    '''
    m = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < m:
            m = arr[i]

    return m

#Driver code
if __name__ == '__main__':
    T = int(input()) # Number of test cases
    for idx in range(T):
        arr = list(map(int, input().split()))
        print(ret_min(arr))
