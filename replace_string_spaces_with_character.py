# Python code to replace the string space with given character
string=input("Enter the string")
result=""
ch=input("enter a character")
for i in string:
    if i==" ":
        i=ch
    result +=i
print("sting result",result)
