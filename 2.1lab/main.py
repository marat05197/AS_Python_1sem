d = eval(input())
print(f"max: {max(d.values())}, min: {min(d.values())}")

for key, value in d.items():
    print(f"key: {key}, value: {value}")

d2 = {'x': list(range(11, 21)), 'y': list(range(21, 31)), 'z': list(range(31, 41))}
print(f"пятый элемент из x: {d2['x'][4]}")
print(f"пятый элемент из y: {d2['y'][4]}")
print(f"пятый элемент из z: {d2['z'][4]}")
