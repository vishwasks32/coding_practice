#!/usr/bin/env python3
# A function that appends one array of integers to another 
# array of integers
# approach 1: just concatenate two lists

def append_array(arr1: list,arr2: list)-> list:
    '''
    Return an appended array of integers 
    '''
    return arr1+arr2
#Driver code
if __name__ == '__main__':
    T = int(input()) # Number of test cases
    for idx in range(T):
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        res_arr = append_array(arr1,arr2)
        for item in res_arr:
            print(item, end=" ")
        print()
