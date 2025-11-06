s = input()
for i in range(1, len(s)):
    if s[i].isalpha() and s[i-1].isalpha() and s[i] < s[i-1]:
        print(i+1)
        break
else:
    print(0)
