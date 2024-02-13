n = int(input())
capacity = 0
at_once = 0

for _ in range(n):
    a, b = map(int, input().split())
    at_once += (b-a)
    capacity = max(capacity, at_once)

print(capacity)
