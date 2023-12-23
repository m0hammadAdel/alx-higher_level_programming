#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None

    list_case = []
    for i in my_list:
        if (i % 2) == 0:
            list_case.append(True)
        else:
            list_case.append(False)
    return list_case
