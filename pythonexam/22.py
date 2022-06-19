
a = {'123 456':9000,'456 789':5000,'789 888':6000,'336 558':10000,'775 666':12000,'566 221':7000}
b = int(input("輸入查詢組數:"))
for i in range(b):
    c = input("輸入帳號密碼:")
    if c in a:
        print(a[c])
    else:
        print('error')
