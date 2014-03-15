#!/bin/sh

FILES="$1*"
HOME="/home/mtydykov/NLPLab/repository/RussianDependencyParser/"

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"
cat allData/training/*_annotated > all_train.conll
cat allData/test/*_annotated > all_test.conll

python add_coarse_pos_tags.py 'all_train.conll'
python add_coarse_pos_tags.py 'all_test.conll'
./TurboParser-2.1.0/TurboParser --train --file_train=all_train.conll.coarse  --file_model=russian_dependency_model.model --logtostderr --logtostderr --model_type=basic

./TurboParser-2.1.0/TurboParser --test --evaluate --file_model=russian_dependency_model.model --file_test=all_test.conll.coarse --file_prediction=russian_parse.conll.predicted --logtostderr

./TurboParser-2.1.0/scripts/eval.pl -b -g all_test.conll.coarse -s russian_parse.conll.predicted

