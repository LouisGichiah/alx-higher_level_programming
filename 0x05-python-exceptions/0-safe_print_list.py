#!/usr/bin/python3
def safe_print_list(my_list=[], a=0):
    ret = 0
    for b in range(a):
        try:
            print("{}".format(my_list[b]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
