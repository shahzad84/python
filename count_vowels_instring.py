# Python program to count vowels and consonants in the string

# string=input("Enter a String: ")
# vowels=0
# consonants=0
# for i in string:
#     if i in ("a","e","i","o","u"):
#         vowels+=1
#     elif i.isalpha():
#         consonants+=1
# print("vowels: ",vowels,"consonants: ",consonants)


# string="ggod"
# vowels=0
# consonant=0
# for i in string:
#     if i in ("a","e","i","o","u"):
#         vowels+=1
#     elif i.isalpha():
#         consonant+=1
# print(vowels,consonant)

sting="good"
vowel=0
const=0
for i in sting:
    if i in ("a","i","o","u"):
        vowel+=1
    elif i.isalpha():
        const+=1
print(vowel,const)
