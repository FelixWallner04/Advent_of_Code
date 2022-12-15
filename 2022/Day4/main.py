import csv
reader = csv.reader(open("day4_input.txt", "r"))

# list and Variables
inputDay4 = []
inputTest = [['2-4', '6-8'], ['2-3', '4-5'], ['5-7', '7-9'], ['2-8', '3-7'], ['6-6', '4-6'], ['2-6', '4-8']]
splitInput = []
p1 = 0
p2 = 0

for line in reader:
    inputDay4.append(line)
#print(inputDay4)

for elm in inputDay4:
    s1, e1 = elm[0].split('-')
    s2, e2 = elm[1].split('-')
    s1, e1, s2, e2 = [int(x) for x in [s1, e1, s2, e2]]
    # (s1,e1) fully contains (s2,e2) and (s2,e2) fully contains (s1,e1)
    if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
        p1 += 1
    # (s2,e2) overlaps (s1,e1) if it is not completely to the left or to the right
    if not (e1 < s2 or e2 < s1):
        p2 += 1
print(p1)
print(p2)
