import sys
f = open(sys.argv[1])
filename = sys.argv[1]+"_post_processed"
f2 = open(filename, 'w+')
print filename
extra_punct = ",.()*&^%$#@!~`-={}[]\|;:\"'?/,.<>"
for line in f:
    line.strip()
    append = ""
    if len(line) > 2:
        line = line.strip()
        if line[0] in extra_punct:
            f2.write(line[0]+"\n")
            line = line[1:]
        if line[-1] in extra_punct:
            append = line[-1]
            line = line[:-1]
    f2.write(line)
    if append != "":
       f2.write("\n")
    f2.write(append+"\n")
f2.close()
    

