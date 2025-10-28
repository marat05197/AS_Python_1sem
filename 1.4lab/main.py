N, A, B = int(input()), int(input()), int(input())
lst = [A, B]
for i in range(2, N):
    lst.append(sum(lst[:i]))
print(lst)
