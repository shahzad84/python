# Algorithm to count alphabets, digits, and special characters in the string


# string = input("Enter a String : ")
# alphabets=0
# digits=0
# specialChars=0
# #checks for each character in the string
# for i in string: 
#     if i.isalpha():
#         alphabets+=1
#     elif i.isdigit():
#         digits+=1
#     else:
#         specialChars+=1
# print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)

# string="good"
# alpha=0
# digit=0
# special=0
# for i in string:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         special+=1

# print(alpha,digit,special)


# string="good"
# alpha=0
# digit=0
# special=0
# for i in string:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         special+=1
# print(alpha,digit,special)

string="good"  
alpha=0
digit=0
special=0
for i in string:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
    else:
        special+=1
print(alpha,digit,special)
