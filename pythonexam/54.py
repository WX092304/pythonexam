a = float(input("請輸入里程公里數(km):"))
sum = 75
if a > 1.5:
    if (a-1.5)<0.25:
        sum += 5
    else:
        if (a-1.5)%0.25==0:
            b=(a-1.5)/0.25*5
            sum += b
        else:
            b=(a-1.5)//0.25*5
            sum = sum + b + 5
print("所需車資為",round(sum))