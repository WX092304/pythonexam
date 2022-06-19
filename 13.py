a = str(input('輸入一字元為:'))
list1 = list(a)
list2 = list(a)
list2.reverse()

if list2 == list1:
    print("YES")
else:
    print("NO")