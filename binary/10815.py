n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
have = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end);

for i in range(m):
    result = binary_search(card, have[i], 0, n-1);
    if result != None:
        print(1, end=' ')
    else:
        print(0, end=' ')