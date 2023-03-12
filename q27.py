file_name = input("Enter the input file name:")
file_obj = open(file_name)
unique_words = []
for line in file_obj:
    words = line.split()
for curr_word in words:
    curr_word = curr_word.strip(',.?!')
if curr_word not in unique_words:
    unique_words.append(curr_word)
file_obj.close()
unique_words.sort()
print()
for curr_word in unique_words:
    print(curr_word)