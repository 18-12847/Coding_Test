import sys
x, y = [], []
for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    if a in x:
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)
print(*x, *y)