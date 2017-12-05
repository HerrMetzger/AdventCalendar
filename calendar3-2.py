import sys

size = int(sys.argv[1])
memory = []
even = False

def addNeighbours(memory,x,y):
    nSum = 0
    for i in range(3):
        xi=i-1
        for j in range(3):
            yj=j-1
            nSum+=memory[y-yj][x-xi]
    return nSum   

def mvUp(x,y):
    y-=1
    return x, y
def mvDn(x,y):
    y+=1
    return x,y
def mvLf(x,y):
    x-=1
    return x, y
def mvRt(x,y):
    x+=1
    return x,y

for i in range(size):
    memory.append([0])
    for j in range(size):
        if j == 0:
            pass
        else:
            memory[i].append(0)
        
if size % 2 == 0:
    even = True
    y0=int(size/2)
    x0=int(size/2-1)
else:
    y0=int((size-1)/2)
    x0=int((size-1)/2)


memory[y0][x0] = 1

for i in range(size):
    for j in range(2):
        for k in range(i):
            print("i is:",i)
            if (i+1) % 2 == 0:
                if   j==0:
                    x0, y0 = mvRt(x0, y0)
                elif j==1:
                    x0, y0 = mvUp(x0, y0)
            else:
                if j==0:
                    x0, y0 = mvLf(x0, y0)
                elif j==1:
                    x0, y0 = mvDn(x0, y0)
            print(x0, y0)
            memory[y0][x0]=addNeighbours(memory,x0,y0)
            for lines in memory:
                print(lines)
