# 8.4 Open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split() method. The program
# should build a list of words. For each word on each line check to see if the
# word is already in the list and if not append it to the list. When the program
# completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

# Use words.txt as the file name
file_name = raw_input("Enter file name: ")
try:
    fh = open(file_name)
except:
    print 'File cannot be openned: ',file_name
    exit()

individual_words = list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in individual_words :
            individual_words.append(word)

individual_words.sort()
print individual_words
