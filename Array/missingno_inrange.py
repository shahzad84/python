# Python Program to find missing number in array
# arr=[]
# n = int(input("enter size of array : "))
# for x in range(n-1):
#     x=int(input("enter element of array : "))
#     arr.append(x)
# sum = (n*(n+1))/2;
# sumArr = 0
# for i in range(n-1):
#     sumArr = sumArr+arr[i];
# print(int(sum-sumArr))


arr=[]
n = int(input("enter size of array : "))
for x in range(n-1):
    x=int(input("enter element of array : "))
    arr.append(x)
sum = (n*(n+1))/2;
sumArr = 0
for i in range(n-1):
    sumArr = sumArr+arr[i];
print(int(sum-sumArr))


