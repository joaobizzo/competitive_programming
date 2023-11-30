n = int(input())
solution = 0
for _ in range(n):
    v = str(input())
    v = int(v[0]) + int(v[2]) + int(v[4])
    if v >= 2:
        solution += 1

print(solution)