# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word
# in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt


file_name = raw_input("Enter file name: ")
try:
    fh = open(file_name)
except:
    print 'File cannot be openned: ',file_name
    exit()

count = 0

for line in fh:
    if line.startswith('From ') :
        line = line.rstrip()
        elements = line.split()
        print elements[1]
        count = count + 1

print "There were", count, "lines in the file with From as the first word"
