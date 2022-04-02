n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
quest = list(map(int, input().split()))

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
    count = 0
    answer = search(card, quest[i], 0, n-1)
    if answer == None:
        pass
    else:
        count += 1

    print(count, end=' ')

# 오류 해결해야함!