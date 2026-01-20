def heart():
    for i in range(N):
        for j in range(N):
            if cookie[i][j] == '*':
                return i + 2, j + 1
            
def left(x, y):
    count = 0
    while y >= 0 and cookie[x][y] == '*':
        count += 1
        y -= 1

    return count

def right(x, y):
    count = 0
    while y < N and cookie[x][y] == '*':
        count += 1
        y += 1

    return count

def lower(x, y):
    count = 0
    while x < N and cookie[x][y] == '*':
        count += 1
        x += 1

    return count
            
N = int(input())
cookie = [[] * N for _ in range(N)]

for i in range(N):
    cookie[i] = input()

heartX, heartY = heart() # 심장의 위치

x = heartX - 1
y = heartY - 1

waist = lower(x+1, y)

body = [left(x, y-1), right(x, y+1), lower(x+1, y), lower(x+waist+1, y-1), lower(x+waist+1, y+1)]

print(heartX, heartY)
print(*body)