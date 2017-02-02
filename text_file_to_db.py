import sys

from model import Entry
from text_tools import *

if __name__ == '__main__':
    text_file = sys.argv[1]
    f = open(text_file, 'r')
    entry = None
    last_section = None
    for line in f:
        line = line.strip()
        if is_new_entry(line):
            if entry is not None:
                entry.save()
            entry = Entry()
            last_section = None

        elif is_arxiv_id(line):
            entry.arxiv_id = get_arxiv_id(line)
            last_section = None  #
        elif is_title(line):
            entry.title = get_title(line)
            last_section = 'title'
        elif is_date(line):
            entry.date = get_date(line)
        elif is_authors(line):
            entry.authors = get_authors(line)
            last_section = 'authors'
        elif is_categories(line):
            entry.categories = get_categories(line)
            last_section = 'categories'
        elif is_empty(line):
            last_section = None
        elif is_double_backslash(line):
            last_section = None
        elif is_section(line):
            pass
        elif is_last_line(line):
            pass
        else:
            if last_section is None:
                last_section = 'abstract'
                entry.abstract = line.strip()
            elif last_section == 'title':
                entry.title += ' ' + line
            elif last_section == 'categories':
                entry.categories += ' ' + line
            elif last_section == 'authors':
                entry.authors += ' ' + line
            elif last_section == 'abstract':
                entry.abstract += ' ' + line
            else:
                pass

    entry.save()
