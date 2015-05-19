# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 1 - process

# copy a list into a new list, implement function 0 
def copy(input_list):
	new_list = input_list
	return new_list

# combine two list
def combine(list1, list2):
    list_combine = []
    for i in list1:
        list_combine.append(i)
    for i in list2:
        list_combine.append(i)
    remove_duplicate_element(list_combine) #注意这里我重用了已有的轮子(去重函数)
    return list_combine

def remove_duplicate_element(list):
    i = 0
    while i <= len(list) - 1:
        j = i + 1
        while j <= len(list) - 1:
            if list[i] == list[j]:
                del list[j]
            j += 1
        i += 1

# common elements in two list
def common(list1, list2):
    list_common = []
    for i in list1:
        for j in list2:
            if j == i:
                list_common.append(j)
    return list_common

# list minus
def minus(list1, list2):
	return list(set(list1) - set(list2))