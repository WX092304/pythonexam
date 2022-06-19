a = list(map(int,input("輸入一組四位數字為:")))
for i in range (len(a)):
    a[i] = (a[i] + 7 ) % 10
print(a)

tmp1 = a[0]
a[0] = a[2]
a[2] = tmp1

tmp2 = a[1]
a[1] = a[3]
a[3] = tmp2

print("輸入加密後的數字為{0}{1}{2}{3}".format(a[0],a[1],a[2],a[3]))