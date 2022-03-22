# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# def dfs(x, y):
#     # 주어진 범위 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or i <= -1 or y >= m:
#         return False
#
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# # 모든 노드에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 dfs 수행
#         if dfs(i, j) == True:
#             result += 1
#
# print(result)

graph = [] # 2차원 리스트 선언

n, m = map(int, input().split()) # 행, 열 입력 받기
for _ in range(n):
    graph.append(list(map(int, input())))

answer = 0 # 답으로 쓸 변수 초기화

def dfs(x, y):
    if x <= -1 or x >= n or y < 0 or y >= m:  # 범위 벗어나면 종료
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True


dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)
