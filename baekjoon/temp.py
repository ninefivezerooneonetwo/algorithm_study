h, m = map(int, input().split())
mp = int(input())
result = m + mp
hp = result // 60 # 시간 더하는 것
mm = result % 60 # 분 더한 후

if result < 60:
    print(h, result)
else:
    if h == 23:
        print(0, mm)
    else:
        print(h+hp, mm)
