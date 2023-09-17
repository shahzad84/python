# Program to Replace first occurrence of Vowel with ‘-‘ in String
def replace_vowel(string):
    vowels="aeiouAIOUE"
    for i in range(len(string)):
        if string[i] in vowels:
            string=string[:i]+"-"+string[i+1:]
            break
    return string


string=input("ente a string : ")
print("original string : ",string)
print("modified string: ", replace_vowel(string))