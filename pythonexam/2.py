a = int(input("輸入度數:"))
if a <= 120:
    print("Summer month:%.2f" % (a*2.10))
    print("Non-Summer month:%.2f" % (a*2.10))
elif a > 121 and a <= 330:
    print("Summer month:%.2f" % (a*3.02))
    print("Non-Summer month:%.2f" % (a*2.68))
elif a > 331 and a <= 500:
    print("Summer month:%.2f" % (a*4.39))
    print("Non-Summer month:%.2f" % (a*3.61))
elif a > 501 and a <= 700:
    print("Summer month:%.2f" % (a*4.97))
    print("Non-Summer month:%.2f" % (a*4.01))
elif a > 700:
    print("Summer month:%.2f" % (a*5.63))
    print("Non-Summer month:%.2f" % (a*4.50))
