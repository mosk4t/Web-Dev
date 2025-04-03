n = int(input())
power = 1
while power < n:
    power *= 2
print("YES" if power == n else "NO")