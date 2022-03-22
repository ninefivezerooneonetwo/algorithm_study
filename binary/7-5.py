n = int(input())
store = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

store.sort()

def search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        result = search(array, target, start, mid - 1)
    # elif array[mid] < target:
    #     search(array, target, mid + 1, end)
    else:
        result = search(array, target, mid + 1, end)

    return result

for i in range(m):
    answer = search(store, want[i], 0, n-1)
    # if type(result) != int:
    #     print("no", end=' ')
    # else:
    #     print("yes", end=' ')
    
    if answer != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')