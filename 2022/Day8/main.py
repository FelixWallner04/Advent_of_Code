import csv
reader = csv.reader(open("day8_input.txt", "r"))

Grid = []
sol1 = 0

for line in reader:
    row = line[0]
    Grid.append(row)

Direction = [(-1,0), (0,1), (1,0), (0, -1)]
maxRow = len(Grid)
maxCol = len(Grid[0])


for row in range(maxCol):
    for col in range(maxRow):
        visuell = False
        for (dr, dc) in Direction:
            rr = row
            cc = col
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0 <= rr < maxRow and 0 <= cc < maxCol):
                    break
                if Grid[rr][cc] >= Grid[row][col]:
                    ok  = False
            if ok:
                visuell = True
        if visuell:
            sol1 += 1
print(sol1)


sol2 = 0
vtlr = 0 # visible trees left and right
vthb = 0 # visible trees top and bot

for row in range(maxCol):
    for col in range(maxRow):
        score = 1
        for (dr, dc) in Direction:
            distance = 1
            rr = row
            cc = col
            while True:
                rr += dr
                cc += dc
                if not (0 <= rr < maxRow and 0 <= cc < maxCol):
                    distance -= 1
                    break
                if Grid[rr][cc] >= Grid[row][col]:
                    break
                distance += 1
            score *= distance
        sol2 = max(sol2, score)
print(sol2)

# with help https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/8.py
