n = int(input('請輸入n:'))
k = int(input('請輸入k:'))

sum = 0
if k > 1:
    while n > 1:
        sum += n
        n = n // k
        if n == 1:
            sum += n

print("Peter可以抽",sum,"支紙菸")