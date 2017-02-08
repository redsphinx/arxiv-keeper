import os
import re
import subprocess
import sys

from sqlalchemy import func, or_
from termcolor import colored

from model import session, Entry
from settings import CHOICE_STRING, KEYWORDS

template_string = """
Remaining: \t%d
Title: \t\t %s
Abstract: \t %s
""" + CHOICE_STRING + """
Make a choice"""

clauses = ()
for keyword in KEYWORDS:
    clauses += (func.lower(Entry.title).like("%%%s%%" % keyword), func.lower(Entry.abstract).like("%%%s%%" % keyword),)

entries = session \
    .query(Entry) \
    .filter(or_(*clauses)) \
    .filter(Entry.abstract != None) \
    .filter(Entry.read != True) \
    .all()

count = session \
    .query(func.count(Entry)) \
    .filter(or_(*clauses)) \
    .filter(Entry.abstract != None) \
    .filter(Entry.read != True) \
    .one()

total = int(count[0])
print total

for entry in entries:
    os.system('clear')

    title = entry.title
    abstract = entry.abstract
    # @TODO it doesn't highlight if there is a uppercase character in word.
    for keyword in KEYWORDS:
        title = title.replace(keyword, colored(keyword, 'red'))
        abstract = abstract.replace(keyword, colored(keyword, 'red'))
    print template_string % (total, title, abstract)
    user_input = sys.stdin.readline()
    entry.read = True
    session.add(entry)
    session.commit()
    if re.match(r'.*[1-4].*', user_input):
        p = subprocess.Popen(['python', 'downloader.py', entry.arxiv_id, user_input])
    if re.match(r'.*q.*', user_input):
        break
    total -= 1
