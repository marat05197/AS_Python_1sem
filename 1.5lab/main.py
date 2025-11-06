arr = list(map(int, input().split()))
result = sorted([arr[i] for i in range(0, len(arr), 2)])
print(result)
