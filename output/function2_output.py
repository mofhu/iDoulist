# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 2 - output

# input - list
# process - ?
# output - a doulist with content in list

import pyautogui
import time

pyautogui.PAUSE = 1 # 1.5 second pause after each call

# first test

# 添加内容 = 519, 386
# 获取网页内容 = 708, 543
# 添加 = 726,713

test_list = ['http://book.douban.com/subject/1059751/',
'http://book.douban.com/subject/1223043/',
'http://book.douban.com/subject/26326498/',
'http://book.douban.com/subject/25967509/',
'http://book.douban.com/subject/10352395/',
'http://book.douban.com/subject/6047885/',
'http://book.douban.com/subject/25850377/',
'http://book.douban.com/subject/2370630/',
'http://book.douban.com/subject/1898860/',
'http://book.douban.com/subject/26288194/',
'http://book.douban.com/subject/25881360/']

print test_list

def output_doulist(input_list):
	# first change focus in browser
	pyautogui.click(519, 386)
	for i in input_list:
		# add  
		time.sleep(5)
		pyautogui.click(519, 386)
		time.sleep(3)
		pyautogui.typewrite(i)
		pyautogui.press('enter')
		time.sleep(5)
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('enter')

output_doulist(test_list)
