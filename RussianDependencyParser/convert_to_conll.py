import sys
f = open(sys.argv[1])
filename = sys.argv[1]+"_post_processed"
f2 = open(filename+".conll", 'w+')
tokenNum = 1
for line in f:
    token_tag = line.split('\t')
    #token id, form, lemma, coarse POS tag, POS tag, features, head, dependency relation, projective head, dependency relation to projective head
    f2.write(str(tokenNum) + '\t' + token_tag[0] + '\t' + '_' + '\t' + '_' + '\t' + token_tag[1].strip() + '\t' + '_' + '\t' + str(tokenNum) + '\t' + '_' + '\t' + '_' + '\t' + '_' + '\n')
    tokenNum += 1
    if token_tag[1].strip() == 'SENT':
        f2.write('\n')
        tokenNum = 1
f.close()
