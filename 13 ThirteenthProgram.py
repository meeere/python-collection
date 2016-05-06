# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.


file_name = raw_input("Enter file name: ")
try:
    fh = open(file_name)

except:
    print 'File cannot be openned: ',file_name
    exit()

count = 0
times = dict()


for line in fh:
    if line.startswith('From ') :
        elements = line.split()
        time = elements[5]
        hour = time.split(':')

        if hour[0] not in times :
            times[hour[0]] = times.get(hour[0],0) + 1
        else :
            times[hour[0]] = times[hour[0]] + 1

lst = list()
for key, val in times.items() :
    lst.append( (key, val) )

lst.sort()

for key,val in lst :
    print key,val
