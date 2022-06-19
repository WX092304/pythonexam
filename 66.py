a = input("請輸入string_a:")
b = input("請輸入string_b:")

set1 = set(a)
set2 = set(b)
c = set1 & set2
list1 = list(c)
list1.sort()
if len(list1)==0:
    print("N")
else:
    for i in range(len(list1)):
        print(list1[i],end="")