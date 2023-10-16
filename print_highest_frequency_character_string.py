# Python program to print the highest frequency character in a String.
# string=input("enter a string: ")
# freq_dist={}
# for char in string: 
#     if char in freq_dist:
#         freq_dist[char]+=1
#     else:
#         freq_dist[char]=1
# max_freq=max(freq_dist.values())


# print the character with maximun frequency
# for char in freq_dist:
#     if freq_dist[char]==max_freq:
#         print(char,end=" ")

# string="hii"
# dist={}
# for char in string:
#     if char in dist:
#         dist[char]+=1
#     else:
#         dist[char]=1
# maxs=max(dist.values())

# for char in dist:
#     if dist[char]==maxs:
#         print(char)

# a="hii"
# dist={}
# for char in a:
#     if char in dist:
#         dist[char]+=1
#     else:
#         dist[char]=1

# maxs=max(dist.values())     

# for char in dist:
#     if dist[char]==maxs:
#         print(char)


a="hii"
dis={}
for i in a:
    if i in dis:
        dis[i]+=1
    else:
        dis[i]=1
maxs=max(dis.values())
for i in dis:
    if dis[i]==maxs:
        print(i)
