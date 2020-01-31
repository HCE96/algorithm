import sys

Num=eval(input())

S=[]

for i in range(Num):
    a=sys.stdin.readline().split()
    if a[0]=="push":
        S.append(a[1])
    elif a[0]=="top":
        if not S:
            print(-1)
        else:
            print(S[len(S)-1])
    elif a[0]=="pop":
        if not S:
            print(-1)
        else:
            print(int(S.pop()))
    elif a[0]=="size":
        print(len(S))
    elif a[0]=="empty":
        if not S:
            print(1)
        else:
            print(0)