from ast import In
a = input("請輸入第一個數字:")
b = input("請輸入第二個數字:")

list1 = list(a)
list2 = list(b)

A = 0
B = 0
if len(list1) >= 2 and len(list1) <= 6:
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            A += 1
        elif list1[i] in list2:
            B += 1
    if A == len(list1) and b == 0:
        print("{0}A{1}B".format(A,B),"全對")
    else:
        print("{0}A{1}B".format(A,B),"加油")