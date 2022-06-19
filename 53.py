a = int(input("輸入n值:"))
dict1 = {}
for i in range(a):
    name = input("請輸入姓名:")
    mail = input("請輸入電子郵件:")
    dict1[name] = mail
name1 = input("請輸入要查詢電子郵件的姓名:")
print("{0}電子郵件帳號為{1}".format(name1,dict1.get(name1))) 
