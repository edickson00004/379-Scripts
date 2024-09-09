
sortList = [5, 1, 7, 3, 1, 3, 9, 3]

sortList.sort()
currentStreak = 0
maxStreak = 0 
maxNum = 0

for i in range (len(sortList)-1):
    if (sortList[i] != sortList[i+1]):
        if (currentStreak > maxStreak):
            maxStreak = currentStreak
            maxNum = sortList[i]
    else:
        currentStreak += 1

print(maxNum)

