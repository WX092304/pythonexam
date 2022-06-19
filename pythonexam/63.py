n = int(input("請輸入正整數n:"))

fac = []
for i in range(1,n):
    if n % i == 0:
        fac.append(i)

sum = 0
for i in range(len(fac)):
    sum += fac[i]
if n == sum:
    print('perfect')
elif n < sum:
    print('abundant')
elif n > sum:
    print('deficient')
