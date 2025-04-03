n, *arr = map(int, input().split())
print(' '.join(str(x) for x in arr if x % 2 == 0))