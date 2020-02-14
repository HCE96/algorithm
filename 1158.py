import sys

number=sys.stdin.readline().split()

number=list(map(int,number))

init=list(range(1,number[0]+1))

result=[]

num=number[1]

while True:

    factor=init.pop(num-1)

    result.append(factor)

    if not init:
        break

    num=num+number[1]-1

    while num>len(init):
        num-=len(init)

print("<",end="")
for i in range(len(result)):
    if i==len(result)-1:
        print(result[i],end=">")
    else:
        print(result[i],end=", ")

