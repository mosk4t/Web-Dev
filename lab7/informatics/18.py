x = int(input())
dividers = []
for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        dividers.append(i)
        if i != x // i:
            dividers.append(x // i)
dividers.sort()
print(' '.join(map(str, dividers)))