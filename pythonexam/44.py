t = int(input())
list1 = []
if t >= 1 and t <= 10:
    for i in range(t):
        a = int(input())
        list1.append(a)
    
print(max(list1))