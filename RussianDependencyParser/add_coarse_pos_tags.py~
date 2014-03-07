import sys
import os
f = open(sys.argv[1])
f2 = open(sys.argv[1]+".coarse", 'w+')
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
for sent in sentences:
    f3 = open('temp', 'w+')
    for line in sent:
        if line != "\n":
            #write each token on a separate line for POS tagger
            line_to_write = line.split('\t')[1]+'\n'
            f3.write(line_to_write)

    f3.close()
    os.system('/home/mtydykov/NLPLab/repository/RussianDependencyParser/tree-tagger/bin/tree-tagger /home/mtydykov/NLPLab/repository/RussianDependencyParser/tree-tagger/russian-small.par temp temp_coarse -token')

    f4 = open('temp_coarse')
    for i, line in enumerate(f4):
        token_tag = line.split('\t')
        token_all_elements = sent[i].split('\t')
    #token id, form, lemma, coarse POS tag, POS tag, features, head, dependency relation, projective head, dependency relation to projective head
        #new_conll_line = str(token_all_elements[0]) + '\t' + token_all_elements[1] + '\t' + '_' + '\t'  + token_tag[1].strip() + '\t' + token_all_elements[4] + '\t' +  '_' + '\t' + token_all_elements[6] + '\t' + '_' + '\t' + '_' + '\t' + '_' + '\n'
	new_conll_line = str(token_all_elements[0]) + '\t' + token_all_elements[1] + '\t' + '_' + '\t'  + token_tag[1].strip() + '\t' + '_' + '\t' +  '_' + '\t' + token_all_elements[6] + '\t' + '_' + '\t' + '_' + '\t' + '_' + '\n'
        f2.write(new_conll_line)
    f2.write('\n')
f.close()
f2.close()
f4.close()

