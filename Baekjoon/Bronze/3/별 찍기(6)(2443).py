import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n, 0, -1):
    print((n - i) * " " + (i * 2 - 1) * "*")