# python-
目前就之开展了这些实例， 如果其他人有更好的绘图实例， 欢迎添加到我的仓库， 谢谢。

Help on class DrawHeart in module mydraw:

class DrawHeart(builtins.object)

 |  使用各种方式 绘制 各种爱心
 |  params: input a string(当有些方法需要string的时候)
 |  return: 各种爱心
 
 |  你需要这些函数库
 |  (
 |      from math import pow

 |      import time

 |      import turtle as T

 |      import numpy as np

 |      from matplotlib import pyplot as plt

 |      import random
 |  )
 
 |  如果你的电脑没有， 请安装：
 
 
 |  Methods defined here:
 |  

 |  draw_loop(self)
 |      绘制一个爱心的循环
 |  
 |  draw_tree(self, brance)
 |  
 |  get_draw_KochSnow(self)
 |      扩展
 |      这是一个科赫雪花的实例
 |      默认递归阶数已给
 |      可修改
 |  
 |  get_draw_cherry_tree(self)
 |      扩展
 |      绘制樱花树
 |  
 |  get_draw_double_heart(self)
 |      绘制一个丘比特之间爱心
 |      (一个箭头射穿二个爱心)
 |      调用即可
 |  
 |  get_draw_heart(self)
 |      return draw heart
 |      using the turtle show heart
 |  
 |  get_draw_rose(self, string=None)
 |      扩展
 |      绘制玫瑰
 |      params:    默认为我自己设置的话， 如果想打印你自己的
 |      传参数 string  用空格隔开，默认三句话，
 |  
 |  get_fill_string_heart(self, string)
 |      输入爱心中间填充的话
 |      绘制爱心， 中间可以添加字符
 |      字符 范围 [1 5]
 |      最大支持输入五个字符
 |  
 |  get_math_fun(self, x, y)
 |      return heart math fun
 |  
 |  get_plt_heart(self)
 |      使用plt绘制一个彩色爱心
 |      原理也是心形方程
 |  
 |  get_string_heart(self, string)
 |      params： 输入你需要绘制的话 这个暂时只支持 英文字符串 不支持汉字
 |      return:  string heart
 |  
 |  ggg(self, n, r, d=1)
 |      玫瑰花曲线绘制
 |  
 |  koch(self, length, n)
 |  
 |  petel(self, m)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None

Process finished with exit code 0
