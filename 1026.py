import sys

Num=int(sys.stdin.readline())

A=sys.stdin.readline().split()

A=list(map(int,A))

B=sys.stdin.readline().split()

B=list(map(int,B))

A.sort()

B.sort(reverse=True)

Min=0
for i in range(Num):
    Min=Min+A[i]*B[i]

print(Min)