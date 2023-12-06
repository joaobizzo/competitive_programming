n, k = map(int, input().split(' '))

p = 0

a = list(map(int, input().split(" ")))
for i in range(n):
    if a[i] > k:
        p += 1
print(p)
