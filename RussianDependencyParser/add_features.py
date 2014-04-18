import sys
import os
from pymorphy import *

def replace_param_with_default(param_to_check):
    if param_to_check == "":
        param_to_check = "_"
    return param_to_check

morph = get_morph('pymorphy_dict')
f = open(sys.argv[1])
f2 = open(sys.argv[1]+".coarse", 'w+')
evaluation_mode=sys.argv[2]
annotation_errors = open(sys.argv[1]+'.annotation_errors','w+')
tokenNum = 1
lines = []
sentences = []
add = True
for line in f:
    # if the token is attached to itself, there's an annotation error;
    # skip the sentence
    if line != "\n" and line.split('\t')[6] == line.split('\t')[0] and evaluation_mode == "True":
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
    os.system('/home/mtydykov/NLPLab/repository/RussianDependencyParser/tree-tagger/bin/tree-tagger /home/mtydykov/NLPLab/repository/RussianDependencyParser/tree-tagger/russian-small.par temp temp_coarse -token -lemma')

    f4 = open('temp_coarse')
    for i, line in enumerate(f4):
        lemma1=""
        lemma2=""
        token_tag = line.split('\t')
        coarse_postag_1 = token_tag[1].strip()
        lemma1 = token_tag[2].strip()
        token_all_elements = sent[i].split('\t')
        postag = token_all_elements[4]
        morph_info = morph.get_graminfo(token_all_elements[1].decode('utf-8').upper())
        morph_1 = ""
        
        if postag != "SENT":
            coarse_postag_2 = postag[0]
            morph_2 = postag[1:len(postag)]
        else:
            coarse_postag_2 = postag
            morph_2 = postag
        
	   #takes the first one for now (if there is a choice)
        if morph_info:
            item = morph_info[0]
            morph_1=item['info'].decode('utf-8')
            lemma2=item['lemma'].decode('utf-8').lower()


	    #if for some reason lemma of class/info is empty, 
        #replace with a string of the appropriate conll format
        morph_1 = replace_param_with_default(morph_1)
        lemma1 = replace_param_with_default(lemma1)
        lemma2 = replace_param_with_default(lemma2)
        postag = replace_param_with_default(postag)
        coarse_postag_1 = replace_param_with_default(coarse_postag_1)


			 #token id
        new_conll_line = str(token_all_elements[0]) + '\t'
			 #surface form
        new_conll_line+= token_all_elements[1] + '\t'
                         #lemma from TreeTagger
        new_conll_line+= lemma1 + '\t'
                         #coarse POS tag
        new_conll_line+= coarse_postag_1 + '\t'
                         #detailed POS tag
        new_conll_line+= postag + '\t'
                         #morphology features 1
        new_conll_line+= morph_1 + '\t'
                         #head
        new_conll_line+= token_all_elements[6] + '\t'
                         #dependency relation
        new_conll_line+= '_' + '\t'
                         #projective head
        new_conll_line+= '_' + '\t'
                         #dependency relation to projective head
        new_conll_line+= '_' + '\t'
                         #lemma from pymorphy
        new_conll_line+= lemma2 + '\t'
			 #morphology from splitting detailed POS tags
        new_conll_line+= morph_2 + '\t'
                         #coarse POS tag from splitting detailed POS tag
        new_conll_line+= coarse_postag_2 + '\n'

        f2.write(new_conll_line)
    f2.write('\n')
f.close()
f2.close()
f4.close()

