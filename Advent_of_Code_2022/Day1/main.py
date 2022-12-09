import csv
reader = csv.reader(open("day1_input.txt", "r"))
list = []
listTest = [1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000, 0 ]
sum = []

rowInt = 0
sol = 0

for line in reader:
    if len(line) == 0:
       line.append(0)
    rowInt = int(line[0])
    list.append(rowInt)

# loop through list and add
for elm in list:
    sol = sol + elm
    if elm == 0:
        sum.append(sol)
        sol = 0
print("Part1: MaxValue",max(sum))

# Tag 2
def identifyMaxValue (value):
    maxValue = max(value)
    value.pop(value.index(maxValue))
    return maxValue

max1 = identifyMaxValue(sum)
max2 = identifyMaxValue(sum)
max3 = identifyMaxValue(sum)

score1 = max3 + max2 + max1
print("Part2: MaxValue", score1)
