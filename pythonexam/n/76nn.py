passwd = list(map(int,input("請輸入傳送密碼(6位數):")))

while len(passwd) < 6:
    print("請重新輸入")


for a in passwd:
    for i in range(1,10):
        if (i * 4) % 7 == a:
            passwd = i
            break
print(a)