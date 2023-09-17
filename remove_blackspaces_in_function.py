# Python program to remove spaces from string without inbuilt function
string=input("Enter a string: ")
result=" "
for i in string:
    if i!=" ":
        result+=i

print(result)
