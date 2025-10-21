N = int(input())
A = float(input())
B = float(input())

H = (B - A) / N
points = [A + i * H for i in range(N + 1)]

print(H)
for point in points:
    print(point)
#под переменные N A B нужно подставить свои значения
