import sys

Num=int(sys.stdin.readline().strip())

Numbers=sys.stdin.readline().split()

Numbers=list(set(Numbers))

Numbers=list(map(int,Numbers))

Numbers.sort()

for Number in Numbers:
    print(Number,end=" ")
