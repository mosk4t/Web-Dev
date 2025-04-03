n, *arr = map(int, input().split())
for i in range(n//2):
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
print(' '.join(map(str, arr)))  