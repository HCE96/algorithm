import sys

Num=int(input())

D=[]

for i in range(Num):
    a=sys.stdin.readline().split()
    if a[0]=="push_front":
        D.append(a[1])
    elif a[0]=="push_back":
        D.insert(0,a[1])
    elif a[0]=="pop_front":
        if not D:
            print(-1)
        else:
            print(int(D.pop()))
    elif a[0]=="pop_back":
        if not D:
            print(-1)
        else:
            print(int(D.pop(0)))
    elif a[0]=="size":
        print(len(D))
    elif a[0]=="empty":
        if not D:
            print(1)
        else:
            print(0)
    elif a[0]=="front":
        if not D:
            print(-1)
        else:
            print(D[len(D)-1])
    elif a[0]=="back":
        if not D:
            print(-1)
        else:
            print(D[0])
