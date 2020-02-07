import sys

Num=int(sys.stdin.readline().strip())

Dots=[]

for i in range(Num):
    Dot=sys.stdin.readline().strip().split()
    Dots.append((int(Dot[0]),int(Dot[1])))

Dots.sort(key = lambda word: (word[0], word[1]))

for Dot in Dots:
    print(str(Dot[0])+" "+str(Dot[1]))