a = (input("請輸入時間1(時:分:秒):"))
b = int(input("請輸入時間2(秒):"))
a1 = a.split(":")
bb = b
list1 = list(map(int,a1))

change = list1[0]*60*60+list1[1]*60+list1[2]
print("時間1(",a,")格式轉換後為",change,"秒")

b1=b//3600
b=b-3600*a
b2=b//60
b=b%60
print("時間2({0})={1}:{2}:{3}".format(bb,b1,b2,b))