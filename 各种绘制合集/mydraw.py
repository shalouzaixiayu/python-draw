# -*- coding :  utf-8 -*-
# @Time      :  2020/6/22  22:33
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219


from math import pow
import time
import turtle as T
import numpy as np
from matplotlib import pyplot as plt
import random


class DrawHeart:
    """
    使用各种方式 绘制 各种爱心
    params: input a string(当有些方法需要string的时候)
    return: 各种爱心
    你需要这些函数库
    (
        from math import pow
        import time
        import turtle as T
        import numpy as np
        from matplotlib import pyplot as plt
        import random
    )
    如果你的电脑没有， 请安装：
    """

    def __init__turtle(self, speed=1, screen_color="white"):
        # 实例化一些turtle相对应的控件
        self.t = T.Turtle()
        self.w = T.Screen()
        # self.w.screensize(bg='wheat')  # 画布颜色小麦色
        self.w.screensize(bg=screen_color)
        # t.speed(0)  # 速度最快
        self.t.getscreen().tracer(speed, 0)  # 返回正在绘制的对象 并且加速5
        self.t.pensize(2)
        self.t.hideturtle()

    def get_math_fun(self, x, y):
        """
        return heart math fun
        """
        return (pow(x * 0.05, 2) + pow(y * 0.1, 2) - 1) ** 3 - pow(x * 0.05, 2) * pow(y * 0.1, 3)

    def get_string_heart(self, string):
        """
        params： 输入你需要绘制的话 这个暂时只支持 英文字符串 不支持汉字
        return:  string heart
        """
        print('开始绘制(3s一个)'.center(60, '-'))
        for char in string.split():
            time.sleep(1.5)
            print('\n'.join([''.join([(char[(x - y) % len(char)] if self.get_math_fun(x, y) <= 0
                                       else ' ') for x in range(-30, 30)]) for y in
                             range(12, -12, -1)]))
            time.sleep(2)
            print()
            print('-' * 60)
            print()

    def get_fill_string_heart(self, string):
        """
        输入爱心中间填充的话
        绘制爱心， 中间可以添加字符
        字符 范围 [1 5]
        最大支持输入五个字符
        """
        string = list(string)
        # 对列表进行动态填满5个位置  否则 pop 会出错
        if len(string) < 5:
            index_sub = 5 - len(string)  # 差值
            for i in range(index_sub):  # 向后插
                string.append(' ')
        a2 = []
        for y in range(15, -15, -1):
            a1 = []
            for x in range(-30, 30):
                if -0.75 <= ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0:
                    a1.append('\033[30;47m*\033[0m')
                elif (x == -15) and (y == (10 or 9)):
                    a1.append('\b\033[31;47m')
                elif (x == -16) and (y == (9 or 8)):
                    a1.append('\b\033[31;47m')
                elif (x == -17) and (y == (8 or 7)):
                    a1.append('\b\033[31;47m')
                elif (x == 14) and (y == (10 or 9)):
                    a1.append('\b\033[31;47m')
                elif (x == 15) and (y == (9 or 8)):
                    a1.append('\b\033[31;47m')
                elif (x == 16) and (y == (8 or 7)):
                    a1.append('\b\033[31;47m')
                elif (x == 0) and (y == 2):
                    sts = string.pop(0)
                    a1.append(f'\b\033[31;47m{sts}\033[0m')
                elif (x == 0) and (y == 1):
                    sts = string.pop(0)
                    a1.append(f'\b\033[31;47m{sts}\033[0m')
                elif (x == 0) and (y == 0):
                    sts = string.pop(0)
                    a1.append(f'\b\033[31;47m{sts}\033[0m')
                elif (x == 0) and (y == -1):
                    sts = string.pop(0)
                    a1.append(f'\b\033[31;47m{sts}\033[0m')
                elif (x == 0) and (y == -2):
                    sts = string.pop(0)
                    a1.append(f'\b\033[31;47m{sts}\033[0m')
                else:
                    a1.append(' ')
            a2.append(''.join(a1))

        b = '\n'.join(a2)
        print(b)

    def draw_loop(self):
        """
        绘制一个爱心的循环
        """
        for i in range(200):
            self.t.right(1)
            self.t.fd(1)

    def get_draw_heart(self):
        """
        return draw heart
        using the turtle show heart
        """
        self.__init__turtle()
        self.t.color('gold', 'red')
        self.t.begin_fill()
        self.t.left(140)
        self.t.fd(111.65)
        self.draw_loop()  # 调用循环
        self.t.left(120)
        self.draw_loop()  # 调用循环
        self.t.fd(111.65)
        self.t.end_fill()
        self.w.exitonclick()  # 关闭画布

    def get_draw_double_heart(self):
        """
        绘制一个丘比特之间爱心
        (一个箭头射穿二个爱心)
        调用即可
        """
        self.__init__turtle()
        self.t.color('black', 'red')
        self.t.pensize(5)
        #  绘制二个粘连爱心
        self.t.begin_fill()
        self.t.penup()
        self.t.goto(50, 50)
        self.t.pendown()
        self.t.right(45)
        self.t.goto(100, 0)
        self.t.left(90)
        self.t.fd(120)
        self.t.circle(50, 225)
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()
        self.t.left(135)
        self.t.fd(120)
        self.t.circle(50, 225)
        self.t.seth(90)
        self.t.circle(50, 225)
        self.t.fd(121)
        self.t.end_fill()
        # 绘制丘比特之剑
        self.t.left(56)
        # self.t.pencolor('black')
        # self.t.pensize(3)
        self.t.penup()
        self.t.goto(-210, 40)
        self.t.pendown()
        self.t.goto(0, 80)
        self.t.penup()
        self.t.goto(160, 110)
        self.t.pendown()
        self.t.goto(320, 140)
        # 绘制箭头
        self.t.left(150)
        self.t.fd(50)
        self.t.penup()
        self.t.goto(320, 140)
        self.t.pendown()
        self.t.left(60)
        self.t.fd(50)
        self.w.exitonclick()

    def get_plt_heart(self):
        """
        使用plt绘制一个彩色爱心
        原理也是心形方程
        """
        style = {"渐变橙色": "autumn",
                 "渐变紫色": "cool",
                 "渐变晚霞": "magma",
                 "渐变彩虹": "rainbow"}
        print("更多色调选择， 请访问plt散点图API")
        for key, values in style.items():
            print(f'系列:{key} 关键词:{values}')
        choose = input("输入选择的系列的关键词:")
        x_np = np.linspace(- 100, 100, 500)
        y_np = np.linspace(- 100, 100, 500)
        points = []
        for y in y_np:
            for x in x_np:
                if self.get_math_fun(x, y) <= 0:
                    points.append({"x": x, "y": y})
        heart_x = list(map(lambda point: point["x"], points))
        heart_y = list(map(lambda point: point["y"], points))
        plt.scatter(heart_x, heart_y, s=10, alpha=0.5, c=range(len(heart_x)), cmap=choose)
        plt.show()

    def ggg(self, n, r, d=1):
        """
        玫瑰花曲线绘制
        """
        for i in range(n):
            self.t.left(d)
            self.t.circle(r, abs(d))

    def get_draw_rose(self, string=None):
        """
        扩展
        绘制玫瑰
        params:    默认为我自己设置的话， 如果想打印你自己的
        传参数 string  用空格隔开，默认三句话，
        """
        if string == None:
            print_str = "我们不需要过多解释 只需要一如既往 奔跑、奔跑、继续奔跑！！"
        else:
            print_str = string
        s1, s2, s3 = print_str.split()[0], print_str.split()[1], print_str.split()[2]
        self.__init__turtle(screen_color="wheat")
        # 初始位置设置
        s = 0.2  # size
        self.t.pencolor("Tan")
        self.t.fillcolor("red")
        self.t.speed(100)
        self.t.penup()
        self.t.goto(0, 900 * s)
        self.t.pendown()
        # 绘制花朵形状
        self.t.begin_fill()
        self.t.circle(200 * s, 30)
        self.ggg(60, 50 * s)
        self.t.circle(200 * s, 30)
        self.ggg(4, 100 * s)
        self.t.circle(200 * s, 50)
        self.ggg(50, 50 * s)
        self.t.circle(350 * s, 65)
        self.ggg(40, 70 * s)
        self.t.circle(150 * s, 50)
        self.ggg(20, 50 * s, -1)
        self.t.circle(400 * s, 60)
        self.ggg(18, 50 * s)
        self.t.fd(250 * s)
        self.t.right(150)
        self.t.circle(-500 * s, 12)
        self.t.left(140)
        self.t.circle(500 * s, 110)
        self.t.left(27)
        self.t.circle(650 * s, 100)
        self.t.left(130)
        self.t.circle(-300 * s, 20)
        self.t.right(123)
        self.t.circle(220 * s, 57)
        self.t.end_fill()
        # 绘制花枝
        self.t.left(120)
        self.t.fd(280 * s)
        self.t.left(115)
        self.t.circle(300 * s, 33)
        self.t.left(180)
        self.t.circle(-300 * s, 33)
        self.ggg(70, 225 * s, -1)
        self.t.circle(350 * s, 104)
        self.t.left(90)
        self.t.circle(200 * s, 105)
        self.t.circle(-500 * s, 63)
        self.t.penup()
        self.t.goto(150 * s, -10 * s)
        self.t.pendown()
        self.t.left(160)
        self.ggg(20, 2400 * s)
        self.ggg(220, 250 * s, -1)
        # 绘制一个绿色叶子
        self.t.fillcolor("green")
        self.t.penup()
        self.t.goto(670 * s, -180 * s)
        self.t.pendown()
        self.t.right(140)
        self.t.begin_fill()
        self.t.circle(300 * s, 120)
        self.t.left(60)
        self.t.circle(300 * s, 120)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(180 * s, -550 * s)
        self.t.pendown()
        self.t.right(85)
        self.t.circle(600 * s, 40)
        # 绘制第二个绿色叶子
        self.t.penup()
        self.t.goto(-150 * s, -1000 * s)
        self.t.pendown()
        self.t.begin_fill()
        self.t.right(120)
        self.t.circle(300 * s, 115)
        self.t.left(75)
        self.t.circle(300 * s, 100)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(430 * s, -1070 * s)
        self.t.pendown()
        self.t.right(30)
        self.t.circle(-600 * s, 35)
        # 文字部分
        self.t.pensize(4)
        self.t.pencolor("purple")
        self.t.penup()
        self.t.goto(-800 * s, -200 * s)
        self.t.pendown()
        self.t.write(f"{s1}", align="left", font=("arial", 10, "normal"))
        self.t.penup()
        self.t.goto(-800 * s, -300 * s)
        self.t.pendown()
        self.t.write(f"{s2}", align="left", font=("arial", 10, "normal"))
        self.t.penup()
        self.t.goto(-750 * s, -400 * s)
        self.t.pendown()
        self.t.write(f"{s3}", align="left", font=("arial", 10, "normal"))
        self.w.exitonclick()

    def petel(self, m):
        # m为循环次数
        # 绘制树叶
        self.t.pensize(2)
        for i in range(m):
            a = 250 - 500 * random.random()  # 树叶长度，有正有负，可以确定海龟走二个方向
            b = 10 - 20 * random.random()  # 树叶宽度
            self.t.penup()
            self.t.fd(b)
            self.t.left(90)
            self.t.fd(a)
            self.t.pendown()
            self.t.pencolor("lightcoral")  # 珊瑚色
            self.t.circle(1)
            self.t.penup()
            self.t.backward(a)
            self.t.right(90)
            self.t.backward(b)

    def draw_tree(self, brance):
        # 画树枝部分
        # brance 分支
        if brance > 4:
            if 8 <= brance <= 16:
                if random.randint(0, 2) == 0:
                    self.t.pencolor("snow")
                else:
                    self.t.pencolor("lightcoral")  # 珊瑚色
                self.t.pensize(brance / 4)
            elif brance < 8:
                if random.randint(0, 1) == 0:
                    self.t.pencolor("snow")
                else:
                    self.t.pencolor("lightcoral")  # 珊瑚色
                self.t.pensize(brance / 2)
            else:
                self.t.pencolor("Tan")  # 褐色
                self.t.pensize(brance / 10)  # 缩小支柱
            self.t.fd(brance)
            a = 1.5 * random.random()
            self.t.right(20 * a)
            b = 1.5 * random.random()
            self.draw_tree(brance - 10 * b)  # 往右画，直到画不动为止，然后左转随机度数
            self.t.left(40 * a)  # 左转
            self.draw_tree(brance - 10 * b)  # 往左画，直到画不动为止，然后右转随机度数
            self.t.right(20 * a)
            self.t.penup()
            self.t.backward(brance)
            self.t.pendown()

    def get_draw_cherry_tree(self):
        """
        扩展
        绘制樱花树
        """
        self.__init__turtle(speed=10, screen_color="wheat")
        self.t.pensize(5)
        self.t.left(90)
        self.t.penup()
        self.t.backward(250)
        self.t.pendown()
        self.t.color("Tan")  # 褐色
        self.draw_tree(70)  # 第一颗桃花，支柱设置80
        self.petel(250)  # 花瓣250
        self.w.exitonclick()  # 点击关闭画布

    def koch(self, length, n):
        # 长度 和 阶数
        if n == 0:
            self.t.fd(length)
        else:
            for i in [0, 60, -120, 60]:
                self.t.left(i)
                self.koch(length / 3, n - 1)

    def get_draw_KochSnow(self):
        """
        扩展
        这是一个科赫雪花的实例
        默认递归阶数已给
        可修改
        """
        self.__init__turtle(speed=30, screen_color="wheat")
        self.t.penup()
        self.t.pensize(2)
        self.t.goto(-200, 100)
        self.t.down()
        Leave = 8
        self.koch(400, Leave)
        self.t.right(120)
        self.koch(400, Leave)
        self.t.right(120)
        self.koch(400, Leave)
        self.t.right(120)
        self.w.exitonclick()


a = DrawHeart()
# a.get_string_heart(string="hello world")
# a.get_fill_string_heart(string='天高任鸟飞')
# a.get_draw_heart()
# a.get_draw_double_heart()
# a.get_plt_heart()
# a.get_draw_rose(string=None)
# a.get_draw_KochSnow()
a.get_draw_cherry_tree()