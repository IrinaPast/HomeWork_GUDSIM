def my_func(arg1,arg2,arg3):
    if arg1 < arg2: min = arg1
    else:  min == arg2
    if arg3 < min: min = arg3
    s = arg1 + arg2 +arg3 -min
    return s
print(my_func(3,5,7))