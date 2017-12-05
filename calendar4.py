import sys


def duplicateChecker(passwordList):
    duplicate = False
    for word1 in range(len(passwordList)):
        for word2 in range(len(passwordList)):
            if word1 != word2 and passwordList[word1] == passwordList[word2]:
                duplicate = True
            else:
                pass
    return duplicate

validSum = 0
with open(sys.argv[1]) as f:
    for line in f:
        passList = line.split()
        duplicate = duplicateChecker(passList)
        if duplicate == False:
            validSum += 1
        else:
            pass

print("Valid passphrases:",validSum)
