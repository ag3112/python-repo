from functools import reduce


def func(a, b):
    if isinstance(a, tuple):
        out = abs(a[0] - a[1]) + abs(b[0] - b[1])
    else:
        out = a + abs(b[0] - b[1])
    return out


lst1, lst2 = [], []
while True:
    try:
        num1, num2 = input().split(' ')
    except:
        break
    lst1.append(int(num1))
    lst2.append(int(num2))

lst1.sort()
lst2.sort()
z = list(zip(lst1, lst2))

ans = reduce(func, z)
print(ans)
