# Python Program to Remove Repeated Character from String
# def remove_duplicate(s):
#     unique_chars=[]
#     for char in s:
#         if char not in unique_chars:
#             unique_chars.append(char)
#     return "".join(unique_chars)
# string=input("enter a string: ")
# print(remove_duplicate(string))

# def dup(s):
#     unique=[]
#     for i in s:
#         if i not in unique:
#             unique.append(i)
#     return "".join(unique)
# string="hiihiiiis"
# print(dup(string))


# def dup(s):
#     unique=[]
#     for i in s:
#         if i not in unique:
#             unique.append(i)
#     return "".join(unique)
# s="jii"
# print(dup(s))


# def dup(s):
#     unique=[]
#     for i in s:
#         if i not in unique:
#             unique.append(i)
#     return "".join(unique)
# a="hii"
# print(dup(a))

def dup(s):
    unique=[]
    for i in s:
        if i not in unique:
            unique.append(i)
    return "".join(unique)
a="hii"
print(dup(a))



