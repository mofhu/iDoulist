# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 2 - output

# input - list
# process - ?
# output - a doulist with content in list

import pyautogui
import time

pyautogui.PAUSE = 0.5 # 1 second pause after each call by pyautogui

def output_doulist(input_list):
    # 1. find button and change focus in browser
    button_pos = pyautogui.locateOnScreen('output/add_button.png')
    if not button_pos: 
        # no valid button        
        print 'No valid button found in screen, please check before import to Doulist.'
        return
    elif len(list(pyautogui.locateAllOnScreen('output/add_button.png'))) > 1:
        # more than one valid button
        print 'More than one button found in screen, please check before import to Doulist.'
        return
    else:
        # valid input: only one button available
        # remaining issue: the picture is not alwas found in screen...that's strange.
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
    print 'Output to Doulist at screen finished.'

