# Python Program to find duplicate numbers in an array.

arr, occur = [], [];
n = int(input("please enter the size of array: "))
for x in range(n):
    occur.append(0)
for x in range(n):
    element = int(input(f"please enter the element of array element between 0 to {n-1} :"))
    arr.append(element)
    occur[arr[x]]=occur[arr[x]]+1
for x in range(n):
    if occur[x]>1:
        print(f"{x} is repeated {occur[x]} times")