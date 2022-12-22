import csv
reader = csv.reader(open("day9.txt", "r"))

DR = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
DC = {'L': -1, 'R': 1, 'U': 0, 'D': 0}

H = (0,0)
T = [(0,0) for _ in range(9)]
S1 = set([T[0]])
S2 = set([T[8]])


for line in reader:
    row = line[0].split()
    dic = row[0]
    dis = int(row[1])

    for _ in range (dis):
        H = (H[0] + DR[dic], H[1] + DC[dic])
        # Part 1
        if abs(H[1]-T[0][1]) >= 2 or abs(H[0]-T[0][0]) >= 2:
            T[0] = (H[0] - DR[dic], H[1] - DC[dic])
        # Part 2
        for i in range (1, 9):
            dr = T[i-1][0] - T[i][0]
            dc = T[i-1][1] - T[i][1]
            if abs(dr) <= 1 and abs(dc) <= 1:
                pass
            elif abs(dr) >= 2 and abs(dc) >= 2:
                T[i] = (T[i][0]-1 if T[i][0]>T[i-1][0] else T[i][0]+1, T[i][1]-1 if T[i][1]>T[i-1][1] else T[i][1]+1)
            elif abs(dr) >= 2:
                T[i] = (T[i][0]-1 if T[i][0]>T[i-1][0] else T[i][0]+1, T[i][1])
            elif abs(dc) >= 2:
                T[i] = (T[i][0], T[i][1]-1 if T[i][1]>T[i-1][1] else T[i][1]+1)
        S1.add(T[0])
        S2.add(T[8])

print(len(S1), S1)
print(len(S2))

# Part 2 outputs a wrong solution
