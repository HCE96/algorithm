import sys

Text=input()

TextNum=len(Text)

Cursor=len(Text)

Num=eval(input())

for i in range(Num):
    a=sys.stdin.readline().split()
    if a[0]=="L":
        if Cursor != 0:
            Cursor=Cursor-1
    elif a[0]=="D":
        if Cursor!=TextNum:
            Cursor=Cursor+1
    elif a[0]=="B":
        if Cursor!=0:
            Text=Text[0:Cursor-1]+Text[Cursor:]
            Cursor=Cursor-1
    elif a[0]=="P":
        Text=Text[0:Cursor]+a[1]+Text[Cursor:]
        Cursor=Cursor+1
    print(Text)


print("".join(Text))