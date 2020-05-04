# Slicing check

user_str = "aabbcc"
sub_str1 = user_str[2:]
sub_str2 = user_str[1:4]
sub_str3 = user_str[1::2]
sub_str4 = user_str[:-2]

print(sub_str1)     # Line 1
print(sub_str2)     # Line 2
print(sub_str3)     # Line 3
print(sub_str4)     # Line 4

index_int = 0
print(user_str[index_int], user_str[index_int+2]) # Line 5


#(a) What is the output produced by Line 1?
#(b) What is the output produced by Line 2?
#(c) What is the output produced by Line 3?
#(d) What is the output produced by Line 4?
#(e) What is the output produced by Line 5?
