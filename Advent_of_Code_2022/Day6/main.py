import csv

reader = csv.reader(open("day6_input.txt", "r"))

message = []
count1 = 0
count2 = 0
index = 0

for line in reader:
    elm = line[0]
    for i in range(0, len(elm), 1):
        count1 += 1
        if not (elm[i] == elm[i + 1] or elm[i] == elm[i + 2] or elm[i] == elm[i + 3] or elm[i + 1] == elm[i + 2] or elm[
            i + 1] == elm[i + 3] or elm[i + 2] == elm[i + 3]):
            break
    count1 += 1;
    message.append(elm[0:14])
    for i in range(14, len(elm), 1):
        count2 += 1
        for j in range(len(message[0]), 0, -1):
            if message[0].count(message[0][14 - j]) == 1 or message[0].count(message[0][14 - j]) == 0:
                index += 1
        if index == 14:
            break
        if len(message[0]) >= 14:
            message[0] = message[0][1:]

        message[0] += elm[i]
        index = 0
    count2 += 13
print("Solution 1:", count1)
print("Solution 2:", count2)
