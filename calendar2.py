import sys

sum = 0
sum2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        varList = line.split()
        varList = list(map(int, varList))
        varMax = max(varList)
        varMin = min(varList)
        sum += (varMax - varMin)

        for i in varList:
            for j in varList:
                if i != j:
                    if i%j == 0:
                        sum2 += i / j
                    else:
                        pass
                else:
                    pass
       
    print("Sum of all:",sum)
    print("Sum of divisives:" , sum2)
