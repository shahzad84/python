# Convert Lowercase vowels to Uppercase using replace() method
# string=input("Enter a string: ")
# vowels="aeiou"
# for char in string:
#     if char in vowels:
#         upper_char=char.upper()
#         string=string.replace(char,upper_char)
# print(string)


# string="good"
# vowels="aeiou"
# for char in string:
#     if char in vowels:
#         upper=char.upper()
#         string=string.replace(char,upper)
# print(string)


# string="good"
# vowel='aeiou'
# for i in string:
#     if i in vowel:
#         upper=i.upper()
#         string=string.replace(i,upper)
# print(string)


# string="good"
# vowel="aeiou"
# for i in string:
#     if i in vowel:
#         upper=i.upper()
#         string=string.replace(i,upper)
# print(string)

string="good"
vowel="aeiou"
for i in string:
    if i in vowel:
        upper=i.upper()
        string=string.replace(i,upper)
print(string)
