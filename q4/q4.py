#!/usr/bin/env python3
from stackapi import StackAPI
from functools import reduce
if __name__ == "__main__":
    words=input().split(sep=' ')
    #tags=reduce(lambda x,y: x+' '+y,words)
    tags='python and numpy'
    SITE=StackAPI('stackoverflow')
    questions=SITE.fetch('questions',tagged=tags,max=20,sort='votes')
    #print(questions)
    for ele in questions['items']:
        print(ele['tags'])
