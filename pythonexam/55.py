booka=['飢餓遊戲3','解憂雜貨店','怪獸與他們的產地','哈利波特6','我的阿富汗筆友','祈念之樹','樓下的房客','小王子']
bookb=['房思琪的初戀樂園','等一個人咖啡','鬼滅之刃14','神農嘗百草','麥田捕手','老人與海','傲慢與偏見','與神同行']
a = input("請輸入欲租借的書籍:")
if a in booka:
    print("在書架A的第",booka.index(a)+1,"本")
elif a in bookb:
    print("在書架B的第",bookb.index(a)+1,"本")
else:
    print("查無此書籍")