# Python program to find all non repeating characters in the string
# string = input('Please enter a string: ')
# freq_dict = {}
# for char in string:
#     if char in freq_dict:
#         freq_dict[char] += 1
#         print(freq_dict)
#     else:
#         freq_dict[char] = 1
# non_repeating_chars = ""
# for char in string:
#     if freq_dict[char] == 1:
#         non_repeating_chars += char
# print("Non-repeating characters:", non_repeating_chars)

# string="hiig"
# dic={}
# for i in string:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# non_rep=""
# for i in string:
#     if dic[i]==1:
#         non_rep+=i
# print(non_rep)


# string="hii"
# dic={}
# for i in string:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# non_rep=""
# for i in string:
#     if dic[i]==1:
#         non_rep+=i
# print(non_rep)


string="ihii"
dic={}
for i in string:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
non_rep=""
for i in string:
    if dic[i]==1:
        non_rep+=i
print(non_rep)
