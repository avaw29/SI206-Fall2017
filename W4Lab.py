import re

fname = "mbox-short.txt"
f = open(fname, "r")
for line in f.readlines():
    if re.search('From', line):
        print (line)
        numbers = re.findall('[0-9]+', line)
        print (numbers)
        name = line.split()[1].split("@")[0]
        print (name)
