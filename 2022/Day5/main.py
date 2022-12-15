import copy
import csv
reader = csv.reader(open("day5_input.txt", "r"))

# List and Variables
S = [
    [],
    ['Q', 'M', 'G', 'C', 'L'],
    ['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
    ['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'],
    ['J', 'F', 'D', 'V', 'Q', 'P'],
    ['N', 'F', 'M', 'S', 'L', 'B', 'T'],
    ['R', 'N', 'V', 'H', 'C', 'D', 'P'],
    ['H', 'C', 'T'],
    ['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'],
    ['Z', 'F', 'H', 'G']
]
stack1 = copy.deepcopy(S)
stack2 = copy.deepcopy(S)
inputPuzzle = []
inputSplit = []
sol1, sol2 = [], []

for line in reader:
    split_line = line[0].split()
    amount_ = int(split_line[1])
    from_ = int(split_line[3])
    to_ = int(split_line[5])
    # Part 1
    for i in range (0, amount_, 1):
        if not (stack1[from_] == []):
            deletedElement = stack1[from_].pop(-1)
            stack1[to_].append(deletedElement)
    # Part 2
    breakIndex = len(stack2[from_])
    countIndex = len(stack2[from_]) - amount_
    for i in range((len(stack2[from_]) - amount_), len(stack2[from_]), 1):
        if countIndex < 0:
            amount_ += 1
            continue
        if countIndex >= breakIndex:
            break
        deletedElement = stack2[from_].pop(countIndex)
        stack2[to_].append(deletedElement)

for i in range(1, len(stack2), 1):
    sol1.append(stack1[i][-1])
    sol2.append(stack2[i][-1])
sol1 = "".join(sol1)
sol2 = "".join(sol2)
print(sol1)
print(sol2)
