#삽입정렬

import sys

Num=int(sys.stdin.readline())

Words=[]

for size in range(Num):
    Num=sys.stdin.readline().strip()
    Words.append(Num)

Words=list(set(Words))

for size in range(1, len(Words)):
    val = Words[size]
    i = size
    while i > 0 and Words[i - 1] > val:
        Words[i] = Words[i - 1]
        i -= 1
    Words[i] = val

for size in range(1,len(Words)):
    length = len(Words[size])
    New=Words[size]
    i = size
    while i > 0 and len(Words[i-1]) > length:
        Words[i] = Words[i - 1]
        i -= 1
    Words[i] = New

for Word in Words:
    print(Word)




