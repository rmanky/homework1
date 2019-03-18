import sys
import time

arg = sys.argv[1]
n = 100000

def timeDiff (initTime):
    print("Total running time for Part 1: ",
          int((time.time() - initTime) * 1000), " milliseconds")

def part1 ():
    sum = 0
    initTime = time.time()
    for x in range(n):
        sum += 1
    timeDiff(initTime)

def part2 ():
    sum = 0
    initTime = time.time()
    for x in range(n):
        for y in range(n):
            sum += 1
    timeDiff(initTime)

def part3 ():
    print("This is part 3")

Questions = {
    "1" : part1,
    "2" : part2,
    "3" : part3
}

Questions.get(arg)()

