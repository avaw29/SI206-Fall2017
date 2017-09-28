fname = "mbox-short.txt"
f = open(fname, "r")
for line in f.readlines():
    if "From" in line:
        print (line)
        name = line.split()[1]
        n = name.split("@")[0]
        print (n)
