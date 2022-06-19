a = input("請輸入A的好友:").split(" ")
b = input("請輸入B的好友:").split(" ")

set1 = set(a)
set2 = set(b)
c = set1 & set2
len = len(c)
print(len)