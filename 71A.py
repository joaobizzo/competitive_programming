#71A
n = input()
for i in range(int(n)):
    word = str(input())
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word) - 2) + word[-1])