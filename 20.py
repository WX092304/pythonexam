a = int(input("組數為:"))
for i in range(1,a+1):
    b = list(input("輸入票數:"))
    print("第",i,"組應收費用:",(int(b[0])*250)+(int(b[2])*175))
