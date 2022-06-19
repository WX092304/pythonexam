a = input("輸入五張牌:").split(" ")
list1 = []
for i in a:
    if i == "A":
        list1.append(int(1))
    elif i == "J":
        list1.append(int(11))
    elif i == "Q":
        list1.append(int(12))
    elif i == "K":
        list1.append(int(13))
    else:
        list1.append(int(i))

sum = 0
for i in list1:
    sum += i
print(sum)