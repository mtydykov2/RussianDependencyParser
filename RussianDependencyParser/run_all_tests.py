import os
import subprocess
import filter_features
def train_and_test_parser(filename, model_type, include_morph=None, include_lemma=None, include_detailed_postags=False, include_coarse_postags=None, no_unk=False):
    subprocess.call('echo "\n MORPH: '+str(include_morph)+'\tLEMMA: ' +str(include_lemma) + '\tDPOS: ' + str(include_detailed_postags) + '\tCPOS: ' + str(include_coarse_postags) + '\tNO_UNK: ' + str(no_unk) + '\tMODEL_TYPE: ' + str(model_type) + '" >> batch_test_corpus_b', shell=True) 
    filter_features.main('all_train.conll.coarse', include_morph, include_lemma, include_detailed_postags, include_coarse_postags, no_unk)                            
    filter_features.main('all_test.conll.coarse', include_morph, include_lemma, include_detailed_postags, include_coarse_postags, no_unk)     
    subprocess.call('./TurboParser-2.1.0/TurboParser --train --file_train=all_train.conll.coarse.parser_input  --file_model=russian_dependency_model.model --logtostderr --model_type='+model_type, shell=True)                        
    subprocess.call('./TurboParser-2.1.0/TurboParser --test --evaluate --file_model=russian_dependency_model.model --file_test=all_test.conll.coarse.parser_input --file_prediction=russian_parse.conll.predicted --logtostderr', shell=True)
    subprocess.call('./TurboParser-2.1.0/scripts/eval.pl -q -g all_test.conll.coarse.parser_input -s russian_parse.conll.predicted >> batch_test_corpus_b', shell=True)
    subprocess.call('echo "----------------------------------------------------------------" >> batch_test_corpus_b', shell=True)


def add_extra_features(model_type, f1, include_morph, include_lemma, include_detailed_postags, include_coarse_postags, no_unk, opts_args_morphy, opts_args_lemmas):
# then try various combinations with other options
# just morphology
    for opts_args in opts_args_morphy:
        include_lemma = None
        include_morph = opts_args
        train_and_test_parser(f1, model_type, include_morph, include_lemma, include_detailed_postags, include_coarse_postags, no_unk)
    # all combos of morphology with lemmas
        for opts_args_2 in opts_args_lemmas:
            no_unk = False
            include_lemma = opts_args_2
            train_and_test_parser(f1, model_type, include_morph, include_lemma, include_detailed_postags, include_coarse_postags, no_unk) # just lemmas
            if include_lemma == "treetagger":
                no_unk = True
                train_and_test_parser(f1, model_type, include_morph, include_lemma, include_detailed_postags, include_coarse_postags, no_unk)
    
    include_morph = None
    for opts_args in opts_args_lemmas:
        no_unk = False
        include_lemma = opts_args
        train_and_test_parser(f1, model_type, include_morph, include_lemma, include_detailed_postags, include_coarse_postags, no_unk)
        if include_lemma == "treetagger":
            no_unk = True
            train_and_test_parser(f1, model_type, include_morph, include_lemma, include_detailed_postags, include_coarse_postags, no_unk)

def test_all(model_type, f1):

    opts_args_morphy = [None, "pymorphy", "treetagger"]
    opts_args_lemmas = [None, "pymorphy","treetagger"] 
    default_starts_detailed = [True,False]
    default_starts_coarse=[None, "spliced", "tagset"]
    no_unk_vals = [True, False]
    
    #test all possible combinations of tool output
    for detailed_val in default_starts_detailed:
        for coarse_val in default_starts_coarse:
            for morph_val in opts_args_morphy:
                for lemmas_val in opts_args_lemmas:
                    # if lemma is from treetagger
                    if lemmas_val=="treetagger":
                        # try out replacing and not replacing unknowns
                        for unk_val in no_unk_vals:
                            train_and_test_parser(f1, model_type, morph_val, lemmas_val, detailed_val, coarse_val, unk_val)
                    #lemma is either empty or from pymorphy; unk_vals should be false
                    else:
                            train_and_test_parser(f1, model_type, morph_val, lemmas_val, detailed_val, coarse_val, False)
         
os.environ["LD_LIBRARY_PATH"] ="$LD_LIBRARY_PATH:/home/mtydykov/NLPLab/repository/RussianDependencyParser/TurboParser-2.1.0/deps/local/lib:"
#subprocess.call('cat allData/training/*_annotated > all_train.conll', shell=True)
#subprocess.call('cat allData/test/*_annotated > all_test.conll', shell=True)

#sort out all info that will go to the parse just once, here
#subprocess.call('python add_features.py all_train.conll', shell=True)
#subprocess.call('python add_features.py all_test.conll', shell=True)


#subprocess.call('echo "Test on Corpus A:" > batch_test', shell=True)
#test_all('basic', 'batch_test')
#test_all('standard', 'batch_test')


subprocess.call('echo "****************************************************************" >> batch_test', shell=True)
subprocess.call('echo "\n\nTest on Test Corpus B:" >> batch_test_corpus_b', shell=True)
subprocess.call('cat allData/dev/*_annotated > all_test.conll', shell=True)

#sort out all info that will go to the parse just once, here
subprocess.call('python add_features.py all_test.conll', shell=True)

test_all('basic', 'batch_test_corpus_b')
test_all('standard', 'batch_test_corpus_b')

#train_and_test_parser('all_train.conll.coarse','basic', include_coarse_postags="spliced")