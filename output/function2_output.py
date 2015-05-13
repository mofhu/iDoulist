# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 2 - output

# input - list
# process - ?
# output - a doulist with content in list

import pyautogui
import time

pyautogui.PAUSE = 1 # 1 second pause after each call by pyautogui

# and more: any robustness?

test_list = ['http://book.douban.com/subject/1059751/',
'http://book.douban.com/subject/1223043/']

print test_list

# test for find button
print pyautogui.locateOnScreen('add_button.png')

def output_doulist(input_list):
    # 1. find button and change focus in browser
    button_pos = pyautogui.locateOnScreen('add_button.png')
    pyautogui.click(button_pos)
    for i in input_list:
        # 2. press button 
        time.sleep(5)
        pyautogui.click(button_pos)
        # 3. write link
        time.sleep(3)
        pyautogui.typewrite(i)
        pyautogui.press('enter')
        # 4. add to Doulist
        time.sleep(5)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

output_doulist(test_list)
