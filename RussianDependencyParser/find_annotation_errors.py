import sys
f = open(sys.argv[1])
annotation_errors = open(sys.argv[1]+'.annotation_errors','w+')
tokenNum = 1
lines = []
sentences = []
add = True
for line in f:
    # if the token is attached to itself, there's an annotation error;
    # skip the sentence
    if line != "\n" and line.split('\t')[6] == line.split('\t')[0]:
        add = False
    lines.append(line)
    if line == "\n":
        if add:
            copy_lines = lines[:]
            sentences.append(copy_lines)
        else:
            for l in lines:
                annotation_errors.write(l)
        del lines[:]
        add = True

annotation_errors.close()
