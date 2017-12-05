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

def anagramChecker(passwordList):
    anagram = False
    for word1 in passwordList:
        for word2 in passwordList:
            wordLength=len(word1)
            wordRisingLength=0
            if len(word1) != len(word2):
                pass
            else:
                for i in word2:
                    for j in word1:
                        if i == j:
                            wordRisingLength+=1
                            break
                        else:
                            pass
                if word1!=word2 and wordRisingLength==wordLength:
                    anagram = True
                    break
        if anagram == True:
            break
        else:
            pass
    return anagram



validSum = 0
with open(sys.argv[1]) as f:
    for line in f:
        passList = line.split()
        duplicate = duplicateChecker(passList)
        anagram = anagramChecker(passList)
        if duplicate == False and anagram == False:
            validSum += 1
        else:
            pass

print("Valid passphrases:",validSum)
