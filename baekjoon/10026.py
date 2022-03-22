n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(str, input())))

def dfs_normal(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 'R':
        graph[x][y] = 1
        for i in range(4):
            dfs_normal(x + dx[i], y + dy[i])
        return True
    elif graph[x][y] == 'G':
        graph[x][y] = 2
        for i in range(4):
            dfs_normal(x + dx[i], y + dy[i])
        return True
    elif graph[x][y] == 'B':
        graph[x][y] = 3
        for i in range(4):
            dfs_normal(x + dx[i], y + dy[i])
        return True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer_normal = 0
for i in range(n):
    for j in range(n):
        if dfs_normal(i, j) == True:
            answer_normal += 1

print(answer_normal)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]