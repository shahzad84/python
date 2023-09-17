# Python Program to count occurrence of characters in string

string=input("please enter string: ")
char=input("please enter character: ")
count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("total no of occurence of ",char,"is: ",count)
