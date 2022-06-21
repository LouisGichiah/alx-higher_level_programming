#!/usr/bin/python3
def safe_print_list_integers(my_list=[], a=0):
    ret = 0
    for b in range(0, a):
        try:
            print("{:d}".format(my_list[b]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)