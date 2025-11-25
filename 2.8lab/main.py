with open('f', 'r') as file_f:
    numbers = list(map(int, file_f.read().split()))

positives = [x for x in numbers if x > 0]
negatives = [x for x in numbers if x < 0]

result = []
for i in range(0, len(positives), 2):
    result.extend(positives[i:i+2])
    result.extend(negatives[i:i+2])

with open('g', 'w') as file_g:
    file_g.write(' '.join(map(str, result)))
