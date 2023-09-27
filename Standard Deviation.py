#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

def Mean(get_data):
    #accumulate([1,2,3])==> a generator ==>list(generator)==>[1,3,6]
    mean=list(itertools.accumulate(get_data))[-1]/len(get_data)
    return "{:.1f}".format(mean)

# Complete the 'stdDev' function below.
def stdDev(get_arr):
    mean=float(Mean(get_arr))
    print(mean)
    squared_distance_from_mean=0
    for i in range(len(get_arr)):
        squared_distance_from_mean+=((get_arr[i]-mean)**2)
    
    variance=squared_distance_from_mean/len(get_arr)
    SD=math.sqrt(variance)
    print("{:.1f}".format(SD))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
