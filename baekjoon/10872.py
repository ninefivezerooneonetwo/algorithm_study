def refac(num):
    result = 1

    if num > 0:
        result = num * refac(num-1)
    else:
        pass
    return result

n = int(input())
print(refac(n))

