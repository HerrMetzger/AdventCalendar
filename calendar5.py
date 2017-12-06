import sys

argList = []
next = 0
current = 0
sum=0

with open(sys.argv[1]) as f:
    for line in f:
        argList += line.split()

argList = list(map(int, argList))

while True:
    try:
        next = argList[current]
        argList[current] = next + 1
        current+=next
        sum+=1
    except IndexError:
        print(sum)
        break
