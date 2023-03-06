# N * N 정사각형
# 시작좌표(1, 1)
# 정사각형 공간 벗어나면 무시
# LRUD(왼, 오, 위, 아래)
# 최종도착지점(X, Y) 공백 구분 출력

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)