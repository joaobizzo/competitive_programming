n, k = input().split(' ')
k = int(k)
p = 0
for value in n:
    a = input()
    for ai in a:
        if ai.isnumeric():
            ai = int(ai)
            

            if ai > k:
                p += 1
print(p)

