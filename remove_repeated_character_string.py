# Python Program to Remove Repeated Character from String
def remove_duplicate(s):
    unique_chars=[]
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)
    return "".join(unique_chars)
string=input("enter a string: ")
print(remove_duplicate(string))
