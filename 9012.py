import sys

num=int(sys.stdin.readline())

for i in range(num):
    sum=0
    P=sys.stdin.readline()
    for i in P:
        if i=="(":
            sum+=1
        elif i==")":
            sum-=1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')