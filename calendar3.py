import sys
import math

slot = int(sys.argv[1])

layer = int(math.sqrt(slot)+.9999)
lastOnLayer = layer**2
firstOnLayer = (layer-1)**2+1
lengthOfLayer = lastOnLayer - firstOnLayer
distFromLast = lastOnLayer - slot 
distFromFirst = slot - firstOnLayer

print("Given slot:",slot,"LOL:", lastOnLayer, "FOL:",firstOnLayer)

if layer % 2 == 0:
    if slot == firstOnLayer or slot == lastOnLayer:
        distance = int((layer/2)+((layer/2)-1))
    elif distFromLast >= layer:
        if distFromFirst >= layer/2:
            offset = distFromFirst - (layer/2-1)
            distance = int(layer/2+offset)
        else:
            offset = (layer/2-1)-distFromFirst
            distance = int(layer/2+offset)
    else:
        if distFromLast >= layer/2:
            offset = distFromLast - (layer/2-1)
            distance = int(layer/2+offset)
        else:
            offset = (layer/2-1)-distFromLast
            distance = int(layer/2+offset)
        
else:
    if slot == firstOnLayer or slot == lastOnLayer:
        distance = int((layer/2)+(layer/2)-1)
    elif distFromLast >= layer:
        if distFromFirst >= layer/2:
            offset = distFromFirst - (layer/2-1)
            distance = int(layer/2+offset)
        else:
            offset = (layer/2-1)-distFromFirst
            distance = int(layer/2+offset)
    else:
        if distFromLast >= layer/2:
            offset = distFromLast - (layer/2-1)
            distance = int(layer/2+offset)
        else:
            offset = (layer/2-1)-distFromLast
            distance = int(layer/2+offset)


print(distance)
