import sys
t = int(sys.stdin.readline())
if t % 10 > 0:
    print("-1")
else:
    a = t // 300
    b = (t - a * 300) // 60
    c = (t - a * 300 - b * 60) // 10
    print(a, b, c) 