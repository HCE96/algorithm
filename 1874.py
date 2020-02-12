import sys

num = int(sys.stdin.readline())

init=[]
stk=[]
result=[]

number=0


for i in range(num):
    init.append(int(sys.stdin.readline()))

print(init)

for i in range(1,num+1):
    stk.append(i)
    result.append("+")

    while number<num and len(stk)!=0 and init[number]==stk[-1]:
        stk.pop()
        result.append("-")
        number+=1

if not stk:
    for i in result:
        print(i)
else:
    print("NO")

