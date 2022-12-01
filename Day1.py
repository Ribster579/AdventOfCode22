from itertools import groupby

# Part#1

calorieList = []
intList = []
sumList = []

with open("CalorieList.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        calorieList.append(line)

res = [list(sub) for ele, sub in groupby(calorieList, key=bool) if ele]

for lst in res:
    lst = list(map(int, lst))
    intList.append(lst)

for element in intList:
    sumList.append(sum(element))

print(max(sumList))

# Part#2

sortedSumLit = sorted(sumList)

print(sum(sortedSumLit[-3:]))
