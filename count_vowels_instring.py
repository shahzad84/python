# Python program to count vowels and consonants in the string

string=input("Enter a String: ")
vowels=0
consonants=0
for i in string:
    if i in ("a","e","i","o","u"):
        vowels+=1
    elif i.isalpha():
        consonants+=1
print("vowels: ",vowels,"consonants: ",consonants)
