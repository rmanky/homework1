import math
import sys

evens = [x for x in range(1, 201) if x % 2 == 0]

def modifiedBinarySearch(k) :
    k = int(k)
    first = 0
    last = len(evens) - 1
    counter = 0
    while(first <= last):
        counter += 1
        middle = math.floor(first + (last-first)/3)
        if(evens[middle] == k):
            print("found k at", middle)
            print("it took", counter, "comparisons")
            exit()
        if(evens[middle] > k):
            last = middle - 1
        if(evens[middle] < k):
            first = middle + 1
    print("k not found")

modifiedBinarySearch(sys.argv[1])
