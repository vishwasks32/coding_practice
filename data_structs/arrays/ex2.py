#!/usr/bin/env python3
# A function that returns last index of the maximum value of an
# array of integers

def ret_max_lst_idx(arr: list)-> int:
    '''
    Return a last index of maximum value in an array of integers
    '''

    # get max value
    max_val = max(arr)
    for i in range(len(arr)-1,0,-1):
        if arr[i] == max_val:
            return i

#Driver code
if __name__ == '__main__':
    T = int(input()) # Number of test cases
    for idx in range(T):
        arr = list(map(int, input().split()))
        print(ret_max_lst_idx(arr))
