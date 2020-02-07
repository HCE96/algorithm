import sys
from collections import Counter

Num1=int(sys.stdin.readline().strip())
Numbers1=sys.stdin.readline().split()
Num2=int(sys.stdin.readline().strip())
Numbers2=sys.stdin.readline().split()

for Number2 in Numbers2:
    print(Numbers1.Counter(Number2),end=" ")