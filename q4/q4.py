#!/usr/bin/env python3
from stackapi import StackAPI
from bs4 import BeautifulSoup
import requests

def check_accepted_answer(d):
    
    pass

def save_to_csv(csv_path):
    pass

if __name__ == "__main__":
    tags=list(map(lambda x: x.lower(),input().split(sep=' ')))
    print(tags)
    SITE=StackAPI('stackoverflow')
    questions=SITE.fetch('questions',tagged=tags,max=50,sort='votes')
    for ele in questions['items']:
        if all(x in ele['tags'] for x in tags):
            pass
