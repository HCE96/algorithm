import sys

Num=eval(input())

Q=[]

for i in range(Num):
    a=sys.stdin.readline().split()
    if a[0]=="push":
        Q.insert(0,a[1])
    elif a[0]=="pop":
        if not Q:
            print(-1)
        else:
            print(int(Q.pop()))
    elif a[0]=="size":
        print(len(Q))
    elif a[0]=="empty":
        if not Q:
            print(1)
        else:
            print(0)
    elif a[0]=="front":
        if not Q:
            print(-1)
        else:
            print(Q[len(Q) - 1])
    elif a[0] == "back":
        if not Q:
            print(-1)
        else:
            print(Q[0])