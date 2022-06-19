n = int(input())
for i in range(n):
    for x in range(n):
        k = int(input())
        if k%9==0 and k%11==0:
                    print("第",i+1,"個點",k)
        else:
                    print("0")
