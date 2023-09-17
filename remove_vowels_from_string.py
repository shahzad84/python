# Python code to remove vowels from the string
string=input("Enter a string: ")
result=" "
for i in string: 
    if i in ("a","e","i","o","u"):
        i=" "
    result+=i
print(result)
