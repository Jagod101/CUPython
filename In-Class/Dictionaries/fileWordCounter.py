#Zach Jagoda and Daniel Kavesh
#jagod101@chapman.edu, Kavesh@chapman._edu
#Zach - 2274813, Daniel - 2314750
#CPSC 230


#1. Open a file
#2. Count all the words in the file
#3. Print dictionary to user
word_count_dict = {}

def word_counter(text_line):
    import string
    speech = text_line
    speech = speech.lower()
    speech = speech.strip(string.punctuation)
    speech = speech.strip(string.whitespace)
    speech_list = speech.split(' ')
    for string in speech_list:
        #If the string exists in dict
        if string in word_count_dict:
            word_count_dict[string] += 1
        else:
            word_count_dict[string] = 1

def display(word_count_dict):
    total_wc = 0
    for key in word_count_dict:
        total_wc += word_count_dict[key]
        print(key, "-", word_count_dict[key])

    print("\n Total Word Count: ", total_wc)
file_to_open = input("What text file would you like to open?")
temp_file = open(file_to_open, "r")
for line_str in temp_file:
    word_counter(line_str)
    #print(line_str, end='')
temp_file.close()
display(word_count_dict)
#print()
