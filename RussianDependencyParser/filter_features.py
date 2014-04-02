from optparse import OptionParser
import sys
import os

def main(argv, include_morph=None, include_lemma=None, include_detailed_postags=False, include_coarse_postags=None, no_unk=False):
    f1 = open(argv+".parser_input","w")
    f2 = open(argv)
    for i, line in enumerate(f2):
        if line != "\n":
            conll_elements = line.split('\t')
            token_id = conll_elements[0]
            surface_form = conll_elements[1]
            lemma_treetagger = conll_elements[2]
            lemma_pymorphy = conll_elements[10].strip().lower()
            coarse_postag_treetagger_tagset = conll_elements[3]
            coarse_postag_treetagger_spliced_detailed = conll_elements[12].strip()
            detailed_postag_treetagger_tagset = conll_elements[4]
    	    morph_pymorphy = conll_elements[5]
            morph_treetagger = conll_elements[11]
            head = conll_elements[6]
            dep_relation = conll_elements[7]
            proj_head = conll_elements[8]
            dep_rel_proj_head = conll_elements[9].strip()
            morph = "_"
            lemma = "_"
            coarse_postag = "_"
            detailed_postag = "_"
    
    
            if include_morph != None:
                # use pymorphy morph features
                if include_morph == "pymorphy" and morph_pymorphy != "_":
                    morph = morph_pymorphy
                # use treetagger morph features
                elif include_morph == "treetagger" and morph_treetagger != "_":
                    morph = morph_treetagger
            if include_lemma != None:
                # use pymorphy lemmas
                if include_lemma == "pymorphy" and lemma_pymorphy != "_":
                    lemma = lemma_pymorphy
                # use treetagger lemmas
                elif include_lemma == "treetagger" and lemma_treetagger != "_":
                    lemma = lemma_treetagger
                    # sometimes treetagger lemmas unknown - if
                    # so specified, use pymorphy lemmas in these cases
                    if no_unk != False:
                        if lemma == "<unknown>":
                            lemma = lemma_pymorphy
        
            # use default detailed POS tags
            if include_detailed_postags:
                if detailed_postag_treetagger_tagset != "_":
                    detailed_postag = detailed_postag_treetagger_tagset
            if include_coarse_postags != None:
                # split up the detailed POS tags into coarse and morphology
                # and use the coarse part here
                if include_coarse_postags == "spliced" and coarse_postag_treetagger_spliced_detailed != "_":
                    coarse_postag = coarse_postag_treetagger_spliced_detailed
                # use default coarse POS tags
                elif include_coarse_postags == "tagset":
                    coarse_postag = coarse_postag_treetagger_tagset
        
            #token id
            new_conll_line = token_id + '\t'
            #surface form
            new_conll_line+= surface_form + '\t'
            #lemma
            new_conll_line+= lemma + '\t'
            #coarse POS tag
            new_conll_line+= coarse_postag + '\t'
            #detailed POS tag
            new_conll_line+= detailed_postag + '\t'
            #features
            new_conll_line+= morph + '\t'
            #head
            new_conll_line+= head + '\t'
            #dependency relation
            new_conll_line+= dep_relation + '\t'
            #projective head
            new_conll_line+= proj_head + '\t'
            #dependency relation to projective head
            new_conll_line+= dep_rel_proj_head + '\n'
        else:
            new_conll_line = '\n'
        f1.write(new_conll_line)
    
    f1.close()
    f2.close()

#main('/home/mtydykov/NLPLab/repository/RussianDependencyParser/all_train.conll.coarse')
