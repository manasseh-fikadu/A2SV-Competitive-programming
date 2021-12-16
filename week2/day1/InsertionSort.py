#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
        j = arr[n - 1]
        for k in range((n-1),0,-1):
            if j>arr[k-1]:
                arr[k] = j
                print(" ".join([str(i) for i in arr]))
                break
            else:  
                arr[k] = arr[k-1]
                print(" ".join([str(i) for i in arr]))
            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
