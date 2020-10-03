#!/usr/bin/env python3
from stackapi import StackAPI
import numpy as np
#import pprint
#import sys

tags = list(map(str.lower, input().split()))
#print(tags)
#tags = ['python','numpy']
fname = '_'.join(map(str,tags))

SITE = StackAPI('stackoverflow', key='eV18T0ejHKZNnSWR6YDmdQ((')
SITE.page_size = 100
SITE.max_pages = 5
ques = SITE.fetch('questions', tagged=';'.join(map(str,tags)), sort='votes')
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(ques)
#sys.exit()
#print('quota_remaining:', ques['quota_remaining'])
final = []
count = 0
for item in ques['items']:
    
    if count == 50:
    	break

    if 'accepted_answer_id' in item:
        
        qid = item['question_id']
        utag = fname
        link = item['link']
        qtag = '"' + str(item['tags']) + '"'
        ans = link + "/#" + str(item['accepted_answer_id'])

        final.append([qid, utag, link, qtag, ans])
        count += 1

final = np.array(final)

np.savetxt(
    fname + '.csv',
    final,
    fmt='%s',
    delimiter=',', 
    header="question_id,tag,link,tags,accepted_answer",
    comments="")