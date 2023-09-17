# Python program to print the highest frequency character in a String.
string=input("enter a string: ")
freq_dist={}
for char in string: 
    if char in freq_dist:
        freq_dist[char]+=1
    else:
        freq_dist[char]=1
max_freq=max(freq_dist.values())


# print the character with maximun frequency
for char in freq_dist:
    if freq_dist[char]==max_freq:
        print(char,end=" ")