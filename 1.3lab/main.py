n = int(input())
x = float(input())
s = 0
for i in range(n + 1):
    s += (-1) ** i * x ** (2 * i + 1) / (2 * i + 1)
print(s)
