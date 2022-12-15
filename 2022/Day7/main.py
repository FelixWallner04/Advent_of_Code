import csv
from collections import defaultdict
reader = csv.reader(open("day7_input.txt", "r"))

tree = defaultdict(int)
path = []

for line in reader:
    word = line[0].strip().split()
    if word[1] == 'cd':
        if word[2] == '..':
            path.pop()
        else:
            path.append(word[2])
    elif word[1] == 'ls':
        continue
    elif word[0] == 'dir':
        continue
    else:
        sz = int(word[0])
        for i in range(1, len(path)+1):
            tree["/".join(path[:i])] += sz

max_used = 70000000 - 30000000
total_used = tree['/']
need_to_free = total_used - max_used

sol1 = 0
sol2 = 1e9
for k,v in tree.items():
    if v <= 100000:
        sol1 += v
    if v>=need_to_free:
        sol2 = min(sol2, v)
print(sol1)
print(sol2)
