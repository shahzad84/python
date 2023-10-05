# Python program to find sum of integers present in the string

# string=input("enter a string")
# sum=0
# for i in string:
#     if i.isdigit():
#         sum=sum+int(i)
# print("sum = ",sum)


string=input("enter a string: ")
sum=0
for i in string:
    if i.isdigit():
        sum=sum+int(i)
print(sum)

