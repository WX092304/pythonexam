import sys
a = input("檢測的字串(end結束):")
if a == 'end':
    sys.exit("檢測結束")
b = input("檢測的單一字元:")
c = a.count(b)
print('字元%s出現次數為:'%(b),c)
