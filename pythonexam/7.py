m,t = map(int,input("輸入月租費形式及通話時間為").split(","))
if m == 186:
    if t * 0.09 > 186:
        print("通話費為:",round(t*0.09*0.8))
    else:
        print("通話費為:",round(t*0.09*0.9))
elif m == 386:
    if t * 0.08 > 386:
        print("通話費為:",round(t*0.08*0.7))
    else:
        print("通話費為:",round(t*0.08*0.8))
elif m == 586:
    if t * 0.07 > 586:
        print("通話費為:",round(t*0.07*0.6))
    else:
        print("通話費為:",round(t*0.07*0.7))
elif m == 986:
    if t * 0.06 > 986:
        print("通話費為:",round(t*0.06*0.5))
    else:
        print("通話費為:",round(t*0.06*0.6))