n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
want = list(map(int, input().split()))

def search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return search(array, target, start, mid - 1)
    else:
        return search(array, target, mid + 1, end)

for i in range(m):
    answer = search(num, want[i], 0, n-1)
    if answer == None:
        print(0)
    else:
        print(1)