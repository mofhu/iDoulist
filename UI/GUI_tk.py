# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - UI module

from Tkinter import *
def test_button():
	print 'iDoulist output'

root = Tk()
hello = Label(root, text = 'iDoulist') # 绘制一个标签
hello.pack()
test = Button(root, text = 'Output test', command = test_button) #绘制一个按钮, 点击则调用函数
test.pack()
root.mainloop()