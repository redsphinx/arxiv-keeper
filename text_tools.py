import re
from datetime import datetime


def is_new_entry(line):
    if not is_empty(line) and re.match(r'^[-]*$', line):
        return True
    else:
        return False


def is_double_backslash(line):
    return line == '\\\\'


def is_title(line):
    return line.startswith('Title:')


def get_title(line):
    return line[6:].strip()


def is_arxiv_id(line):
    return line.startswith('arXiv:')


def get_arxiv_id(line):
    return re.match(r'([0-9]*\.[0-9]*)', line[6:].strip()).group(0)


def is_date(line):
    return line.startswith('Date:')


def get_date(line):
    return parse_date(re.match(r'^(.*) (\(.*\))*$', line[5:]).group(1).strip())


def is_authors(line):
    return line.startswith('Authors:')


def get_authors(line):
    return line[9:].strip()


def is_categories(line):
    return line.startswith('Categories:')


def get_categories(line):
    return line[12:].strip()


def is_empty(line):
    return line == ''


def is_last_line(line):
    return line.startswith('\\') and re.match(r'.*arxiv\.org.*', line)


def is_continuation(line):
    return line[0] == line[1] == ' '


def parse_date(date_string):
    return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z')


def is_section(line):
    return re.match(r'^[A-Za-z\-]*: .*', line)
