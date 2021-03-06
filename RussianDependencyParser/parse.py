
#usage: python parse.py -f FILE_TO_PARSE

#optional arguments: -m MORPH -l LEMMA N-u -d -c COARSE_POS
#any of the arguments can be excluded 

#MODEL_TYPE can be any one of the TurboParser model types - basic, standard, full
#MORPH can be one of {"pymorphy", "treetagger"}
#LEMMA can be one of {"pymorphy", "treetagger"}
#COARSE_POS can be one of {"split", "tagset"}

#outputs file as filename_postagged.conll


import sys
import filter_features
import subprocess
import os
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-m", dest = "include_morph", default = None, type = "string")
parser.add_option("-l", dest = "include_lemma", default = None, type = "string")
parser.add_option("-d", dest = "include_detailed_postags", default = False,  action='store_true')
parser.add_option("-c", dest = "include_coarse_postags", default = None, type = "string")
parser.add_option("-u", dest = "no_unk", default = False,  action='store_true')
parser.add_option("-f", dest = "filename", default = None,  type = "string")

(options, args) = parser.parse_args()
subprocess.call('bash tokenize_and_pos_tag_file '+options.filename, shell=True)
subprocess.call('python add_features.py '+options.filename+'_postagged.conll False', shell=True)
#use the current best combination of features for the parser
filter_features.main(options.filename+'_postagged.conll.coarse', options.include_morph, options.include_lemma, options.include_detailed_postags, options.include_coarse_postags, options.no_unk)
os.environ["LD_LIBRARY_PATH"] ="$LD_LIBRARY_PATH:TurboParser-2.1.0/deps/local/lib:"
subprocess.call('./TurboParser-2.1.0/TurboParser --test --file_model=russian_dependency_model.model --file_test='+options.filename+'_postagged.conll.coarse.parser_input --file_prediction='+options.filename+'.conll.predicted --logtostderr', shell=True)
