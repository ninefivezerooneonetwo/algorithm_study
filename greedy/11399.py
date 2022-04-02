n = int(input())
minute = list(map(int, input().split()))
minute.sort()

answer = 0

for i in range(n):
    for j in range(i+1):
        answer += minute[j]

print(answer)