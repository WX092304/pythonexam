
a = list(input("輸入值為(0-9):"))
if len(a) <= 0 or len(a) > 7:
    print("輸入個數錯誤")
b = a.sort()
min = ""
for i in range(len(a)):
    min=min+a[i]
c = a.reverse()
max = ""
for i in range(len(a)):
    max=max+a[i]
print("最大值數列與最小值數列差值為:",(int(max)-int(min)))
