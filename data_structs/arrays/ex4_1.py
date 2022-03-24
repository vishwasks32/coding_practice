#!/usr/bin/env python3
# A function that rotates an array given number of positions
def rotate_array(arr: list,n:int)-> list:
    '''
    Return an rotated array of integers 
    '''
    n = n % len(arr)
    new_arr = []
    for i in range(n):
        new_arr[i] = arr[len(arr)-n+i]

    for j in range(n,i < len(arr)):
        new_arr[i] = arr[i - n]

    return new_arr
#Driver code
if __name__ == '__main__':
    T = int(input()) # Number of test cases
    for idx in range(T):
        arr1 = list(map(int, input().split()))
        N = int(input())
        res_arr = rotate_array(arr1,N)
        for item in res_arr:
            print(item, end=" ")
        print()
