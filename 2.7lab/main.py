python
with open('file.txt', 'r') as f:
    lines = f.readlines()

with open('file.txt', 'w') as f:
    f.writelines(lines[1:-1])
