#!/usr/bin/env python3
# Program to demonstrate basics of array using a list
def arr_basic()->None:
    '''
    Function to demonstrate array basic using list
    '''

    # Declare an array
    arr = []
    arr1 = {}
    arr2 = [1,2,3,4]
    arr3 = [[1,2,3],[4,5,6]]

    print(arr2[2])
    print(len(arr3))
    print(arr3[0][2])

if __name__ == '__main__':
    arr_basic()
