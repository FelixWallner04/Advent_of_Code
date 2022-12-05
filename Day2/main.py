import csv
# reading in the date
reader = csv.reader(open("day2.txt", "r"))

# List and Variablen
list = []
splitList = []
listTest = [['A Y'],['B X'],['C Z']]

sol = 0
sumPart1 = 0
sumPart2 = 0
valueP = 0
valueR = 0
i = 0


# the rows of day2.txt file are stored in list
# Format [['A']] -> list in list
for row in reader:
    list.append(row)
print(list)

# pop the last element, because it is a empty element
list.pop(-1)

# String split
for elm in list:
    splitList.append(elm[0].split())
print(splitList)

# Function - Part1: which looks whether you have won - drawn - lost
# A - Rock  |   B - Paper   |   C - Scissors
# X - Rock - 1 P  |   Y - Paper - 2 P   |   Z - Scissors - 3 P
# 0 P - lost  |   3 P - draw    |   6 P - won
def winnerPart1(value1, value2):
    # Rock - Rock | draw and 1 point
    valueR = 0
    if(value1 == "A" and value2 == "X"):
        valueP = 1
        valueR = 3
    # Rock - Paper | win and 2 point
    elif(value1 == 'A' and value2 == 'Y'):
        valueP = 2
        valueR = 6
    # Rock - Scissors | lost and 3 point
    elif (value1 == 'A' and value2 == 'Z'):
        valueP = 3
        valueR = 0
    # Paper - Rock | lost and 1 point
    elif (value1 == 'B' and value2 == 'X'):
        valueP = 1
        valueR = 0
    # Paper - Paper | draw and 2 point
    elif (value1 == 'B' and value2 == 'Y'):
        valueP = 2
        valueR = 3
    # Paper - Scissors | win and 3 point
    elif (value1 == 'B' and value2 == 'Z'):
        valueP = 3
        valueR = 6
    # Scissors - Rock | win and 1 point
    elif (value1 == 'C' and value2 == 'X'):
        valueP = 1
        valueR = 6
    # Scissors - Paper | lost and 2 point
    elif (value1 == 'C' and value2 == 'Y'):
        valueP = 2
        valueR = 0
    # Scissors - Scissors | draw and 3 point
    elif (value1 == 'C' and value2 == 'Z'):
        valueP = 3
        valueR = 3
    sum = sol + valueR + valueP
    valueR = 0
    valueP = 0
    return sum

# Function - Part 2: which looks wheter you have to lose - draw - win
# X - lose  |   Y - draw    |   Z - win
# X - Rock - 1 P |   Y - Paper - 2 P  |   Z - Scissors - 3 P
# 0 - lost  |   3 P - draw    |   6 P - won
def winnerPart2(value1, value2):
    # Rock - lose - Scissors | 0 Round - 3 Points
    valueR = 0
    if(value1 == "A" and value2 == "X"):
        valueP = 3
        valueR = 0
    # Rock - draw - Rock| 3 Round - 1 Point
    elif(value1 == 'A' and value2 == 'Y'):
        valueP = 1
        valueR = 3
    # Rock - win - Paper | 6 Round - 2 Point
    elif (value1 == 'A' and value2 == 'Z'):
        valueP = 2
        valueR = 6
    # Paper - lose - Rock | 0 Round - 1 Point
    elif (value1 == 'B' and value2 == 'X'):
        valueP = 1
        valueR = 0
    # Paper - draw - Paper | 3 Round - 2 Point
    elif (value1 == 'B' and value2 == 'Y'):
        valueP = 2
        valueR = 3
    # Paper - win - Scissors | 6 Round and 3 point
    elif (value1 == 'B' and value2 == 'Z'):
        valueP = 3
        valueR = 6
    # Scissors - lose - Paper | 0 Round - 2 Point
    elif (value1 == 'C' and value2 == 'X'):
        valueP = 2
        valueR = 0
    # Scissors - draw - Scissors | 3 Round and 3 Point
    elif (value1 == 'C' and value2 == 'Y'):
        valueP = 3
        valueR = 3
    # Scissors - win - Rock | 6 Round and 1 Point
    elif (value1 == 'C' and value2 == 'Z'):
        valueP = 1
        valueR = 6
    sum = sol + valueR + valueP
    valueR = 0
    valueP = 0
    return sum

# loops for the actual score
for elm in splitList:
    sumPart1 = sumPart1 + winnerPart1(elm[0], elm[1])
    sumPart2 = sumPart2 + winnerPart2(elm[0], elm[1])
print(sumPart1)
print(sumPart2)

# Tag 2
