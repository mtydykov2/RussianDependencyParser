#!/bin/sh

train_and_test_parser(){
    echo "\n$1 $2" >> batch_test                              
    python filter_features.py 'all_train.conll.coarse' $1
    python filter_features.py 'all_test.conll.coarse' $1
    ./TurboParser-2.1.0/TurboParser --train --file_train=all_train.conll.coarse.parser_input  --file_model=russian_dependency_model.model --logtostderr --logtostderr --model_type=$2

    ./TurboParser-2.1.0/TurboParser --test --evaluate --file_model=russian_dependency_model.model --file_test=all_test.conll.coarse.parser_input --file_prediction=russian_parse.conll.predicted --logtostderr

    ./TurboParser-2.1.0/scripts/eval.pl -q -b -g all_test.conll.coarse.parser_input -s russian_parse.conll.predicted >> batch_test
    echo "----------------------------------------------------------------" >> batch_test
}


test_all(){
#$1 is model type
train_and_test_parser "-d" $1
train_and_test_parser "-c" $1
train_and_test_parser "-c spliced" $1
train_and_test_parser "-d -c" $1 #detailed POS tags and coarse POS tags from default coarse tagset
train_and_test_parser "-d -c spliced" $1 #detailed POS tags and coarse POS tags from default coarse tagset
train_and_test_parser "-d -m " $1
train_and_test_parser "-c" $1
train_and_test_parser "-c spliced" $1
train_and_test_parser "-d -c" $1 #detailed POS tags and coarse POS tags from default coarse tagset
train_and_test_parser "-d -c spliced" $1 #detailed POS tags and coarse POS tags from default coarse tagset
}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home/mtydykov/NLPLab/repository/RussianDependencyParser/TurboParser-2.1.0/deps/local/lib:"
FILES="$1*"
HOME="/home/mtydykov/NLPLab/repository/RussianDependencyParser/"


cat allData/training/*_annotated > all_train.conll
cat allData/test/*_annotated > all_test.conll

#sort out all info that will go to the parse just once, here
python add_features.py 'all_train.conll'
python add_features.py 'all_test.conll'

echo "Test on Test Corpus A:" > batch_test
test_all basic
test_all standard


echo "****************************************************************" >> batch_test
echo "\n\nTest on Test Corpus B:" > batch_test
cat allData/dev/*_annotated > all_test.conll

#sort out all info that will go to the parse just once, here
python add_features.py 'all_test.conll'
test_all basic
test_all standard

