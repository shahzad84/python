# Python program to find all non repeating characters in the string
string = input('Please enter a string: ')
freq_dict = {}
for char in string:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
non_repeating_chars = ""
for char in string:
    if freq_dict[char] == 1:
        non_repeating_chars += char
print("Non-repeating characters:", non_repeating_chars)

