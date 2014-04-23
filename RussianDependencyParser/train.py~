#trains TurboParser with the given features on the default training data
#usage: python train.py -t MODEL_TYPE
#optional arguments: -m MORPH -l LEMMA N-u -d -c COARSE_POS
#any of the arguments can be excluded 

#MODEL_TYPE can be any one of the TurboParser model types - basic, standard, full
#MORPH can be one of {"pymorphy", "treetagger"}
#LEMMA can be one of {"pymorphy", "treetagger"}
#COARSE_POS can be one of {"split", "tagset"}


from optparse import OptionParser
import filter_features
import subprocess
import os

parser = OptionParser()
parser.add_option("-m", dest = "include_morph", default = None, type = "string")
parser.add_option("-l", dest = "include_lemma", default = None, type = "string")
parser.add_option("-d", dest = "include_detailed_postags", default = False,  action='store_true')
parser.add_option("-c", dest = "include_coarse_postags", default = None, type = "string")
parser.add_option("-u", dest = "no_unk", default = False,  action='store_true')
parser.add_option("-t", dest = "model_type", default = None,  type = "string")

(options, args) = parser.parse_args()

subprocess.call('cat allData/training/*_annotated > all_train.conll', shell=True)
subprocess.call('python add_features.py all_train.conll False', shell=True)
filter_features.main('all_train.conll.coarse', options.include_morph, options.include_lemma, options.include_detailed_postags, options.include_coarse_postags, options.no_unk)                        
os.environ["LD_LIBRARY_PATH"] ="$LD_LIBRARY_PATH:TurboParser-2.1.0/deps/local/lib:"       
subprocess.call('./TurboParser-2.1.0/TurboParser --train --file_train=all_train.conll.coarse.parser_input  --file_model=russian_dependency_model.model --logtostderr --model_type='+options.model_type, shell=True)                        

