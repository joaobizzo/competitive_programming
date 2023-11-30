n = int(input())
solution = 0
for p in range(n):
    i = 0
    for _ in range(3):
        if int(input()) == 1:
            i += 1
    if i >= 2:
        solution += 1

print(solution)