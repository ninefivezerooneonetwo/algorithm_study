def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 하지만 피보나치 수열을 이렇게 작성하면 n이 커질수록 수행 시간이 기하급수적으로 늘어난다!
# 시간복잡도 -> O(2의 n승)
# 이러한 문제를 다이나믹 프로그래밍을 사용하여 효율적으로 해결 가능
# 단, 다음 조건을 만족할 때에
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.