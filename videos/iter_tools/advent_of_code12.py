from functools import reduce


def func(a, b):
    if isinstance(a, tuple):
        out = abs(a[0] - a[1]) + abs(b[0] - b[1])
    else:
        out = a + abs(b[0] - b[1])
    return out


lst1, lst2 = [], []
with open('/Users/anks/Documents/abc.txt', 'r') as f:
    for line in f:
        num1, num2 = line.split(' ')
        lst1.append(int(num1))
        lst2.append(int(num2))

out = 0
for num in lst1:
    out = out + (num * lst2.count(num))

print(out)
