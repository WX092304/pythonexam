a = int(input("輸入第一行正整數:"))
list1 = list(map(int,input("第二行中數列中的數字為:").split(" ")))
list2 = set(list1)
list3 = []

if len(list1) == len(list2):
    print("每個數字剛好出現一次")
else:
    for i in list1:
        list3.append(list1.count(i))
    
    maxval = max(list3,default=0)
    indexval = list3.index(maxval)

    print("最大出現次數的數字為",list1[indexval])
    print("出現次數為",maxval)    
