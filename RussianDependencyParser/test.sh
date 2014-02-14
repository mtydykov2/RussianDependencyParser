#!/bin/bash

#usage: sh tokenize_and_pos_tag_file /home/mtydykov/brat-v1.3_Crunchy_Frog/data/test_corpora/WikipediaTestA.txt /home/mtydykov/workspace/RussianDependencyParser/Lingua-RU-OpenCorpora-Tokenizer-0.03/

FILES="$1*"
for f in $FILES
do
    #if [[ "$f" =~ ^[*tokenized*] -a "$f" =~ ^[*postagged*] -a "$f" =~ ^[*post_processed*] -a "$f" =~ ^[*conll*] ]];
    if ! [[ $f == *tokenized* ]]
    then
        
        echo $f
    fi
done
