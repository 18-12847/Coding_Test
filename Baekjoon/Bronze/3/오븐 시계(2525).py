import sys
a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().rstrip())
print((a + ((b + c) // 60)) % 24, (b + c) % 60)