import csv
reader = csv.reader(open("day3_input.txt", "r"))

# List and Variables
input = []
listTest = [['vJrwpWtwJgWrhcsFMMfFFhFp'], ['jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'], ['PmmdzqPrVvPwwTWBwg'], ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'], ['ttgJtRGJQctTZtZT'], ['CrZsJsPPZsGzwwsLwLmpwMDw']]
splitInput = []
rucksack1 = []
rucksack2 = []
sumInput = []
listBadge = []
index = 0
i = 0
j = ''
scr = 0

# Function: to identify the Score of the single chars
# can also be done with array and index() but did not know it at the time
def switch(value):
    scr = 0
    if(value == 'a'):
        scr = 1
    elif (value == 'b'):
        scr = 2
    elif (value == 'c'):
        scr = 3
    elif (value == 'd'):
        scr = 4
    elif (value == 'e'):
        scr = 5
    elif (value == 'f'):
        scr = 6
    elif (value == 'g'):
        scr = 7
    elif (value == 'h'):
        scr = 8
    elif (value == 'i'):
        scr = 9
    elif (value == 'j'):
        scr = 10
    elif (value == 'k'):
        scr = 11
    elif (value == 'l'):
        scr = 12
    elif (value == 'm'):
        scr = 13
    elif (value == 'n'):
        scr = 14
    elif (value == 'o'):
        scr = 15
    elif (value == 'p'):
        scr = 16
    elif (value == 'q'):
        scr = 17
    elif (value == 'r'):
        scr = 18
    elif (value == 's'):
        scr = 19
    elif (value == 't'):
        scr = 20
    elif (value == 'u'):
        scr = 21
    elif (value == 'v'):
        scr = 22
    elif (value == 'w'):
        scr = 23
    elif (value == 'x'):
        scr = 24
    elif (value == 'y'):
        scr = 25
    elif (value == 'z'):
        scr = 26
    elif (value == 'A'):
        scr = 27
    elif (value == 'B'):
        scr = 28
    elif (value == 'C'):
        scr = 29
    elif (value == 'D'):
        scr = 30
    elif (value == 'E'):
        scr = 31
    elif (value == 'F'):
        scr = 32
    elif (value == 'G'):
        scr = 33
    elif (value == 'H'):
        scr = 34
    elif (value == 'I'):
        scr = 35
    elif (value == 'J'):
        scr = 36
    elif (value == 'K'):
        scr = 37
    elif (value == 'L'):
        scr = 38
    elif (value == 'M'):
        scr = 39
    elif (value == 'N'):
        scr = 40
    elif (value == 'O'):
        scr = 41
    elif (value == 'P'):
        scr = 42
    elif (value == 'Q'):
        scr = 43
    elif (value == 'R'):
        scr = 44
    elif (value == 'S'):
        scr = 45
    elif (value == 'T'):
        scr = 46
    elif (value == 'U'):
        scr = 47
    elif (value == 'V'):
        scr = 48
    elif (value == 'W'):
        scr = 49
    elif (value == 'X'):
        scr = 50
    elif (value == 'Y'):
        scr = 51
    elif (value == 'Z'):
        scr = 52
    return scr

# the rows of day3.txt file are stored in list
# Format [['A']] -> list in list
for row in reader:
    input.append(row)
#print(list)


# Part 1:
# Loop to split the string in the middle
# outcome are two list
for i in input:
    index = int(len(i[0]) / 2)
    rucksack1.append(i[0][:index])
    rucksack2.append(i[0][index:])
#print("Rucksack 1: ", rucksack1)
#print("Rucksack 2: ", rucksack2)

# Function: loop through both strings to search for same letter
#str = "p" in rucksack1[0]
#print(str)
index = 0
for i in rucksack1:
    for j in i:
        boolContain = j in rucksack2[index]
        if boolContain:
            sumInput.append(j)
            break
    index += 1

# loop through sum and return score
for elm in sumInput:
    scr = scr + switch(elm)
print( "Part1: Score", scr)


# Part 2:
scr = 0
# loop through 3 strings and looks for same letter
# store same char in listBadge
for i in range(0, len(input), 3):
    for j in input[i][0]:
        bool1 = j in input[i+1][0]
        bool2 = j in input[i+2][0]
        if bool1 and bool2:
            listBadge.append(j)
            break

# print score
for elm in listBadge:
    scr = scr + switch(elm)
print("Part2: Score", scr)