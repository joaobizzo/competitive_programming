# n = participants / k = position / a = score / ai = points / result = how many advence
n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

result = 0
for ai in a:
    if ai >= a[k-1] and ai != 0:
        result += 1

print(result)