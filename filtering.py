import os
import re
import subprocess
import sys
from termcolor import colored

from sqlalchemy import func, or_

from model import session, Entry
from settings import CHOICE_STRING

template_string = """
Remaining: \t%d
Title: \t\t %s
Abstract: \t %s
""" + CHOICE_STRING + """
Make a choice"""

keywords = ['deep', 'learning', 'neural', 'network']
conditions = []
# for keyword in keywords:
#     conditions.append(func.lower(Entry.title).like("%%%s%%"%keyword))
#     conditions.append(func.lower(Entry.abstract).like("%%%s%%"%keyword))
entries = session.query(Entry).filter(or_(
    func.lower(Entry.title).like("%deep%"),
    func.lower(Entry.title).like("%learning%"),
    func.lower(Entry.title).like("%neural%"),
    func.lower(Entry.title).like("%network%"),
    func.lower(Entry.abstract).like("%deep%"),
    func.lower(Entry.abstract).like("%learning%"),
    func.lower(Entry.abstract).like("%neural%"),
    func.lower(Entry.abstract).like("%network%"))
).filter(Entry.abstract != None).filter(Entry.read != True).all()
count = session.query(func.count(Entry)).filter(or_(
    func.lower(Entry.title).like("%deep%"),
    func.lower(Entry.title).like("%learning%"),
    func.lower(Entry.title).like("%neural%"),
    func.lower(Entry.title).like("%network%"),
    func.lower(Entry.abstract).like("%deep%"),
    func.lower(Entry.abstract).like("%learning%"),
    func.lower(Entry.abstract).like("%neural%"),
    func.lower(Entry.abstract).like("%network%"))
).filter(Entry.abstract != None).filter(Entry.read != True).one()
total= int(count[0])
print total


for entry in entries:
    os.system('clear')

    title = entry.title
    abstract = entry.abstract
    for keyword in keywords:
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
