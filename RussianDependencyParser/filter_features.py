
import sys
import os

def replace_param_with_default(bool_to_check, param_to_check):
    if param_to_check == "_" or bool_to_check == '0':
        param_to_check = "_"
    return param_to_check

f1 = open(sys.argv[1]+".parser_input","w")
f2 = open(sys.argv[1])
include_info_string = sys.argv[2]
include_lemma=sys.argv[3]
include_detailed_postag=sys.argv[4]
include_coarse_postag=sys.argv[5]

for i, line in enumerate(f2):
    if line != "\n":
        conll_elements = line.split('\t')
        token_id = conll_elements[0]
        surface_form = conll_elements[1]
        lemma = conll_elements[2]
        coarse_postag = conll_elements[3]
        postag = conll_elements[4]
	info_string = conll_elements[5]
        head = conll_elements[6]
        dep_relation = conll_elements[7]
        proj_head = conll_elements[8]
        dep_rel_proj_head = conll_elements[9].strip()

        info_string = replace_param_with_default(include_info_string,info_string)
        lemma = replace_param_with_default(include_lemma,lemma)
        postag = replace_param_with_default(include_detailed_postag,postag)
        coarse_postag = replace_param_with_default(include_coarse_postag,coarse_postag)

			 #token id
	new_conll_line = token_id + '\t'
			 #surface form
        new_conll_line+= surface_form + '\t'
                         #lemma
        new_conll_line+= lemma + '\t'
                         #coarse POS tag
        new_conll_line+= coarse_postag + '\t'
                         #detailed POS tag
        new_conll_line+= postag + '\t'
                         #features
        new_conll_line+= info_string + '\t'
                         #head
        new_conll_line+= head + '\t'
                         #dependency relation
        new_conll_line+= dep_relation + '\t'
                         #projective head
        new_conll_line+= proj_head + '\t'
                         #dependency relation to projective head
        new_conll_line+= dep_rel_proj_head + '\n'

        f1.write(new_conll_line)
    else:
        f1.write('\n')
f1.close()
f2.close()