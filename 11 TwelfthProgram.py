# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to
# a count of the number of times they appear in the file. After the dictionary
# is produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.


file_name = raw_input("Enter file name: ")
try:
    fh = open(file_name)

except:
    print 'File cannot be openned: ',file_name
    exit()

count = 0
emails = dict()


for line in fh:
    if line.startswith('From ') :
        elements = line.split()
        if elements[1] not in emails :
            emails[elements[1]] = emails.get(elements[1],0) + 1
        else :
            emails[elements[1]] = emails[elements[1]] + 1


print emails
