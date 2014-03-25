#!/bin/sh

train_and_test_parser(){
    echo $1 >> batch_test                              #morph, lemma, detailed, coarse
    python filter_features.py 'all_train.conll.coarse' $2 $3 $4 $5
    python filter_features.py 'all_test.conll.coarse' $2 $3 $4 $5
    ./TurboParser-2.1.0/TurboParser --train --file_train=all_train.conll.coarse.parser_input  --file_model=russian_dependency_model.model --logtostderr --logtostderr --model_type=$6

    ./TurboParser-2.1.0/TurboParser --test --evaluate --file_model=russian_dependency_model.model --file_test=all_test.conll.coarse.parser_input --file_prediction=russian_parse.conll.predicted --logtostderr

    ./TurboParser-2.1.0/scripts/eval.pl -q -b -g all_test.conll.coarse.parser_input -s russian_parse.conll.predicted >> batch_test
    echo "----------------------------------------------------------------" >> batch_test
}


test_all(){
train_and_test_parser "\n$1 model, morph, lemma, detailed POS tags, coarse POS tags:" 1 1 1 1 $1
train_and_test_parser "\n$1 model, nmorph, detailed POS tags, coarse POS tags:" 1 0 1 1 $1
train_and_test_parser "\n$1 model, lemma, detailed POS tags, coarse POS tags:" 0 1 1 1 $1
train_and_test_parser "\n$1 model, morph, lemma, detailed POS tags:" 1 1 1 0 $1
train_and_test_parser "\n$1 model, morph, detailed POS tags:" 1 0 1 0 $1
train_and_test_parser "\n$1 model, lemma, detailed POS tags:" 0 1 1 0 $1
train_and_test_parser "\n$1 model, detailed POS tags:" 0 0 1 0 $1
train_and_test_parser "\n$1 model, coarse POS tags:" 0 0 0 1 $1
train_and_test_parser "\n$1 model, lemma, coarse POS tags:" 0 1 0 1 $1
train_and_test_parser "\n$1 model, morph, coarse POS tags:" 1 0 0 1 $1
train_and_test_parser "\n$1 model, morph, lemma, coarse POS tags:" 1 1 0 1 $1
train_and_test_parser "\n$1 model, detailed POS tags, coarse POS tags:" 0 0 1 1 $1
}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home/mtydykov/NLPLab/repository/RussianDependencyParser/TurboParser-2.1.0/deps/local/lib:"
FILES="$1*"
HOME="/home/mtydykov/NLPLab/repository/RussianDependencyParser/"


cat allData/training/*_annotated > all_train.conll
cat allData/test/*_annotated > all_test.conll

#morphology, lemma, detailed POS tags, coarse POS tags

#sort out all info that will go to the parse just once, here
python add_coarse_pos_tags.py 'all_train.conll'
python add_coarse_pos_tags.py 'all_test.conll'

echo "Test on Test Corpus A:" > batch_test
echo "Just detailed, basic model:" >> batch_test
train_and_test_parser 0 0 1 0 basic
echo "Detailed & coarse, basic model:" >> batch_test
train_and_test_parser 0 0 1 1 basic
echo "Just coarse, basic model:" >> batch_test
train_and_test_parser 0 0 0 1 basic
echo "Just detailed, standard model:" >> batch_test
train_and_test_parser 0 0 1 0 standard
echo "Detailed & coarse, standard model:" >> batch_test
train_and_test_parser 0 0 1 1 standard
echo "Just coarse, standard model:" >> batch_test
train_and_test_parser 0 0 0 1 standard
#test_all basic
#test_all standard


echo "****************************************************************" >> batch_test
echo "\n\nTest on Test Corpus B:" >> batch_test
cat allData/dev/*_annotated > all_test.conll

#sort out all info that will go to the parse just once, here
#python add_coarse_pos_tags.py 'all_test.conll'
#test_all basic
#test_all standard

