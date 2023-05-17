#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_list = my_list[:]
    for i in range(len(replace_list)):
        if replace_list[i] == search:
            replace_list[i] = replace

    return replace_list
