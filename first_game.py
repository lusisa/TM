"""  用python设计第一个游戏 """

temp = input("不妨猜一下我心里现在想的是哪个数字：")
guess = int(temp)

if guess <= 8:
    print("猜对了")
    if guess == 8:
        print("是8")
    else:
        print("不是8")
    print("小循环结束")   
else:
    print("猜错了")

print("游戏结束")
