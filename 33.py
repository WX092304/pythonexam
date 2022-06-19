
list1 = []
list2 = []
a = int(input("國文:"))
list1.append(a)
list2.append("國文")

b = int(input("英文:"))
list1.append(b)
list2.append("英文")

c = int(input("微積分:"))
list1.append(c)
list2.append("微積分")

d = int(input("體育:"))
list1.append(d)
list2.append("體育")

e = int(input("程式設計:"))
list1.append(e)
list2.append("程式設計")

avg1 = (a+b+c+d+e)/5

max = max(list1)
maxindex = list1.index(max)
min = min(list1)
minindex = list1.index(min)

print("平均分數:%.2f"%avg1)
print("最高分科目:{0}{1}分".format(list2[maxindex],max))
print("最低分科目:{0}{1}分".format(list2[minindex],min))
