i = 0
while i < 10:
    print(">" * (i + 1))
    i = i + 1

left, right = ' ', 'o' 
# 符號可修改
layer = 10 
# 可修改階層數量
i = 0
while i < layer:
    lcount = i
    rcount = layer - i
    # 若要更改呈現方式改上述兩點即可
    print(left * lcount + right * rcount)
    i = i + 1

# 練習 倒金字塔
left, middle, right = ' ', 'x', ' ' 
layer = 10
i = 0
while i < 10:
    lcount = i
    mcount = (layer * 2 - 1) - 2 * i
    rcount = i
    print(left * lcount + 
          middle * mcount + 
          right * rcount)
    i = i + 1