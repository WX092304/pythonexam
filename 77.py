with open('data.txt','r') as a:
    content = a.readlines()

list1 = []
list2 = []
for i in content:
    b = i.split(",")
    list1.append(b[0])
    list2.append(b[1])

intlist1 = list(map(int,list1))
intlist2 = list(map(int,list2))

blood = 0
for i in intlist1:
    blood += i
avg1 = blood/len(intlist1)
print("血壓平均:",round(avg1,2))
print("血壓最大值:",max(intlist1))
print("血壓最小值:",min(intlist1))

heart = 0
for i in intlist2:
    heart += i
avg2 = heart/len(intlist2)
print("心跳平均:",round(avg2,2))
print("心跳最大值:",max(intlist2))
print("心跳最小值:",min(intlist2))