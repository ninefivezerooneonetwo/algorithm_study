mylist = [list(map(str, input().split())) for _ in range(8)]
color = '0101010110101010' * 4
new = ""
count = 0

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new += mylist[i][j]

for a, b in zip(new, color):
    if a == 'F' and b == '0':
        count += 1

print(count)




