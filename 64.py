a = int(input("請輸入第一個要判斷的數字:"))
b = int(input("請輸入第二個要判斷的數字:"))
if a % 2 == 1 and (a + 2) % 2 == 1:
    if b % 2 == 1 and (b + 2) % 2 == 1:
        print("Y")
    else:
        print("N")
else:
    print("N") 
