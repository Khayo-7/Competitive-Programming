m = int(input())

for i in range(m):
    n, x1, y1, x2, y2 = map(int, input().split())

    x_y_1 = min(x1, y1, n - x1 + 1,  n - y1 + 1)
    x_y_2 = min(x2, y2, n - x2 + 1,  n - y2 + 1)

    print(abs(x_y_1 - x_y_2))

