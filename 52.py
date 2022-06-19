a = '紅豆生南果，春來發幾枝?願君多采擷，此物最相思。'
b = '春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
a1 = set(a)
b1 = set(b)
c = a1 & b1
c.remove("，")
c.remove("。")
print(c)
