import sys

num=int(sys.stdin.readline())

for i in range(num):
    case=sys.stdin.readline().strip()

    number=int(sys.stdin.readline())

    Arr=eval(sys.stdin.readline())

    error=False
    R_count=0
    D_front=0

    for i in range(len(case)):

        if case[i]=="R":
            R_count+=1

        else:
            try:
                if R_count % 2 == 0:
                    D_front += 1

                else:
                    Arr.pop()
            except:
                error=True
                break

    if error or D_front > len(Arr):
        print('error')
        continue

    if R_count % 2 == 0:
        answer = Arr[D_front:]
    else:
        answer = list(reversed(Arr[D_front:]))



    print("[",end="")
    for i in range(len(answer)):
        if i==len(answer)-1:
            print(str(answer[i]),end="")
        else:
            print(str(answer[i]),end=",")
    print("]")


