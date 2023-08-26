def fact(a):
    if a==0:
        return 1
    else:
        return ((a)*fact(a-1))
num=4
result=fact(num)
print(result)
