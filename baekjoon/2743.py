a, b = map(int, input().split())
people = list(map(int, input().split()))
result = 0

for i in range(len(people)):
    result = people[i] - (a*b)
    print(result, end=" ")