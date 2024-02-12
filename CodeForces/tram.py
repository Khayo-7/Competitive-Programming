# n = int(input())
# capacity = 0
# for _ in range(n):
#     a, b = map(int, input().split())
#     capacity = max(capacity, capacity + (b-a))

#     print(capacity)
# print(capacity)

n, k = map(int, input().split())

while k > 0:

    if n%10 == 0:
        n //= 10
        k -= 1
    else: 
        k -= n%10
        n -= n%10

print(n)