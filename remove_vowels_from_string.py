# Python code to remove vowels from the string
# string=input("Enter a string: ")
# result=" "
# for i in string: 
#     if i in ("a","e","i","o","u"):
#         i=" " #If i is one of the specified vowels, this line sets the value of i to an empty string
#     result+=i
# print(result)


# string="hii this"
# res=""
# for i in string:
#     if i in ("a","i","o","u"):
#         i=""
#     res+=i
# print(res)

string="hii"
result=""
for i in string:
    if i in ("aeiou"):
        i=""
    result+=i
print(result)



